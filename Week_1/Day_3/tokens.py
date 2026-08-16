import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role = "user"

prompt1 = "Hi!"
prompt2 = "What is the weather like today?"
prompt3 = "Write an essay on machine learning in 10 sentences."

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:

    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=200
    )

    usage = response.usage

    print(
        f"prompt: {prompt} --> "
        f"your token usage is: "
        f"prompt_tokens: {usage.prompt_tokens}, "
        f"completion_tokens: {usage.completion_tokens}, "
        f"total_tokens: {usage.total_tokens}, "
        f"Finish Reason: {response.choices[0].finish_reason}"
    )