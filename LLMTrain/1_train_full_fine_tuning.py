import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    set_seed,
)

"""
Train LLM with HuggingFace Trainer (CausalLM)

- Model: Falcon-RW-1B (causal language model)
- Dataset format: JSON with 'messages' (system/user/assistant)
- Template: LLaMA 3-style chat template
- Trainer: HuggingFace `Trainer` + DataCollatorForLanguageModeling
- Goal: Simple SFT (supervised fine-tuning) for chat-style dialogue

Author: yoon
Date: 2025-04-02
"""

# Lamma Training Approch.
LLAMA_3_CHAT_TEMPLATE = (
    "{% for message in messages %}"
        "{% if message['role'] == 'system' %}"
            "{{ message['content'] }}"
        "{% elif message['role'] == 'user' %}"
            "{{ '\n\nHuman: ' + message['content'] + eos_token }}"
        "{% elif message['role'] == 'assistant' %}"
            "{{ '\n\nAssistant: ' + message['content'] + eos_token }}"
        "{% endif %}"
    "{% endfor %}"
    "{% if add_generation_prompt %}"
        "{{ '\n\nAssistant: ' }}"
    "{% endif %}"
)

# Setting
MODEL_NAME = "tiiuae/falcon-rw-1b"
DATA_PATH = "./train_data"
OUTPUT_DIR = "./outputs"
MAX_SEQ_LENGTH = 256

def main():
    # Fix Seed
    set_seed(42)

    # 토크나이저 로드
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.chat_template = LLAMA_3_CHAT_TEMPLATE
    tokenizer.padding_side = "right"

     # Message converts into input_ids/attention_mask
    def convert_to_features(example):
        prompt = tokenizer.apply_chat_template(example["messages"], tokenize=False)
        return tokenizer(prompt, truncation=True, max_length=MAX_SEQ_LENGTH, padding="max_length")

    # load datasets
    dataset = load_dataset("json", data_files={
        "train": os.path.join(DATA_PATH, "train_dataset.json"),
        "test": os.path.join(DATA_PATH, "test_dataset.json")
    })

    dataset = dataset.map(convert_to_features, remove_columns=["messages"])

    print("Converted Length:", dataset["train"].column_names)
    print("Input Length:", len(dataset["train"][0]["input_ids"]))

    # Data collator
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    # Model load
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
        use_cache=True,
    )

    # Training model
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=1,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        logging_steps=10,
        save_strategy="no",
        evaluation_strategy="no",
        bf16=torch.cuda.is_bf16_supported(),
        fp16=torch.cuda.is_available(),
        report_to="none",
        remove_unused_columns=False,
    )

    # Trainer Model
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    # Starts
    trainer.train()

    # save
    trainer.save_model(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Save Model Location:", OUTPUT_DIR)

if __name__ == "__main__":
    main()
