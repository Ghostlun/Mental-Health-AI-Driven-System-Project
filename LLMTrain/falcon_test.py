from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel

# Load tokenizer and base model
base_model = "tiiuae/falcon-rw-1b"
model_path = "./falcon-lora-mental-health"

tokenizer = AutoTokenizer.from_pretrained(base_model)
model = AutoModelForCausalLM.from_pretrained(base_model, device_map="auto")
model = PeftModel.from_pretrained(model, model_path)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device_map="auto")

prompt = "User: I feel so overwhelmed lately and don't know what to do.\nAssistant:"
output = pipe(prompt, max_new_tokens=100, do_sample=True, top_p=0.95, temperature=0.7)

print(output[0]["generated_text"])
