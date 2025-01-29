import os
from groq import Groq

client = Groq(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
