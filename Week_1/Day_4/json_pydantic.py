import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key =os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    issue: str
    email: str

schema=Ticket.model_json_schema()
response_format={
    "type": "json_object"
}
system_prompt=f"""
 Extract the personal information from the ticket strictly based on this schema and give a json output. {schema}
 """
message_system= {"role": "system",
            "content": system_prompt}

text="Hello My name is Pari .I have an iphone which is not working properly. My address is Delhi.My email is pari@example.com.My phone number is 1234567890." 
prompt=f"""
This is a customer ticket. Please extract the personalinformation from the text:{text}
"""
message = {"role": role,
            "content": prompt}
messages = [message_system, message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)



answer=response.choices[0].message.content
print(answer)

#isko padhte kaise hai aage
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)
#inko pass kar skte hai
print(ticket.name)
print(ticket.issue)
print(ticket.email)