import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key =os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b  "
role="user"
prompt="Suggest a name for my cloth company."
message_system={"role": "system",
            "content": "You are a brand manager who suggests name for my company.name should be in one word"}
message = {"role": role,
            "content": prompt}
messages = [message_system, message]
# Temperature is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 2) will result in more random and creative responses, while a lower temperature (e.g., 0.2) will produce more focused and deterministic responses.
response = client.chat.completions.create(model=model, messages=messages, temperature=0)
#print(response)

print("###################")
answer=response.choices[0].message.content
print(answer)