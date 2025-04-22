import os
import torch
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from trl import SFTTrainer
from peft import LoraConfig, get_peft_model, TaskType

MODEL_NAME = "tiiuae/falcon-rw-1b"
DATA_DIR = "./train_data"
OUTPUT_DIR = "./falcon-lora-mental-health"
MAX_SEQ_LENGTH = 512

# === Load Dataset ===
train_df = pd.read_json(f"{DATA_DIR}/train_dataset.json", lines=True)
test_df = pd.read_json(f"{DATA_DIR}/test_dataset.json", lines=True)
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# === Tokenizer ===
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# === Convert Messages to Prompt ===
def apply_template(example):
    messages = example["messages"]
    prompt = ""
    for msg in messages:
        if msg["role"] == "user":
            prompt += f"\nUser: {msg['content']}"
        elif msg["role"] == "assistant":
            prompt += f"\nAssistant: {msg['content']}"
    prompt += "\nAssistant:"
    return tokenizer(prompt, truncation=True, padding="max_length", max_length=MAX_SEQ_LENGTH)

train_dataset = train_dataset.map(apply_template, remove_columns=["messages"])
test_dataset = test_dataset.map(apply_template, remove_columns=["messages"])

# === Load Base Model ===
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

# === Apply LoRA ===
peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    bias="none"
)
model = get_peft_model(model, peft_config)

# === Training Arguments ===
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    fp16=torch.cuda.is_available(),
    save_strategy="epoch",
    logging_steps=10,
    report_to="none",
    evaluation_strategy="epoch"
)

# === Train ===
trainer = SFTTrainer(
    model=model,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer,
    args=training_args,
    dataset_text_field="input_ids",
    packing=False
)

# Save Model Parts
model.save_pretrained("./falcon-lora-mental-health")
tokenizer.save_pretrained("./falcon-lora-mental-health")
