from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import torchvision
# print(torch.__version__)
# print(torchvision.__version__)

# Load the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("advice_model")

# Load the model
model = GPT2LMHeadModel.from_pretrained("advice_model")

# Example usage
input_text = "Question: How can I reduce stress? Topics: Anxiety Diagnosis: Stress Response:"
inputs = tokenizer.encode(input_text, return_tensors="pt")
outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)