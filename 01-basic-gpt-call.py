import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

model_name = "gpt-3.5-turbo"

def chat_with_gpt(system_message, user_message, model_name):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

result = chat_with_gpt("You are dope hip hop MC. Answer the questions in this style!", "What is the capital of Hungary?", model_name)

print(result)