import groq
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the API key from the .env file

client = groq.Groq(api_key=os.getenv("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"))

print("🤖 Welcome to your AI Chatbot! Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who answers in a friendly tone."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content
    print("AI:", reply)
