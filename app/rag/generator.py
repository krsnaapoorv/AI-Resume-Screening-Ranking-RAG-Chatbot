"""LLM answer generation over retrieved context."""

import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"
#
#
# def generate_answer(query: str, context_chunks: list):
#     if not context_chunks:
#         return "No relevant information found in the resume."
#
#     context = "\n".join(context_chunks)
#
#     prompt = f"""
# You are an AI assistant helping evaluate candidates.
#
# Context from resume:
# {context}
#
# Question:
# {query}
#
# Instructions:
# - Answer only based on the context
# - If not mentioned, say "Not mentioned in the resume"
# - Be concise
#
# Answer:
# """
#
#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": "llama3",
#             "prompt": prompt,
#             "stream": False
#         }
#     )
#
#     return response.json()["response"]


from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(query: str, context_chunks: list):
    if not context_chunks:
        return "No relevant information found in the resume."

    context = "\n".join(context_chunks)

    prompt = f"""
You are an AI assistant helping evaluate candidates.

Context from resume:
{context}

Question:
{query}

Instructions:
- Answer ONLY based on the context
- If not mentioned, say "Not mentioned in the resume"
- Be precise and short

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
