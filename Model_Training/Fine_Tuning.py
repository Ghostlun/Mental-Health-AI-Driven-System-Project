import openai
import os
import API_KEY as api

openai.api_key = api.get_API_KEY()
def upload_file():
    response = openai.File.create(
    file=open("openai_training_data_re_2.jsonl", "rb"),
    purpose="fine-tune"
    )
    return response

def create_file():
    response = openai.FineTune.create(
        training_file="file-K7uHn6rYZpyT0Hebs4c0bBAF",  
        model="gpt-3.5-turbo"  # Specify the correct model
    )
    return response

# print(upload_file())
print(create_file())