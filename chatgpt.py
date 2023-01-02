import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="composition pattern in typescript with example",
    temperature=0.3,
    max_tokens=3000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0
)

print(response["choices"][0]["text"])