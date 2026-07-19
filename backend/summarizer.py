from config import client, MODEL
from prompts import (
    SYSTEM_PROMPT,
    SUMMARY_PROMPT,
    BATCH_SUMMARY_PROMPT,
    FINAL_SUMMARY_PROMPT
)
from utils.batching import batch_items
from concurrent.futures import ThreadPoolExecutor


from openai import RateLimitError
import time


def call_llm(messages, retries=5):
    delay = 1
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
            )
            return response.choices[0].message.content

        except RateLimitError:
            if attempt == retries - 1:
                raise
            print(f"Rate limited. Retrying in {delay}s...")
            time.sleep(delay)
            delay *= 2


def summarize_chunk(chunk):
    prompt = SUMMARY_PROMPT.format(text=chunk.page_content)
    return call_llm([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ])


def summarize_chunks(chunks):
    # return [summarize_chunk(chunk) for chunk in chunks]
    with ThreadPoolExecutor(max_workers=2) as executor:
        chunk_summaries = list(executor.map(summarize_chunk, chunks))

    return chunk_summaries


def summarize_batch(batch):
    combined = "\n\n".join(batch)
    prompt = BATCH_SUMMARY_PROMPT.format(text=combined)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def generate_final_summary(chunk_summaries):
    if len(chunk_summaries) <= 5:
        combined_summary = "\n\n".join(chunk_summaries)
        prompt = FINAL_SUMMARY_PROMPT.format(text=combined_summary)
        return call_llm([
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ])
    
    batches = batch_items(chunk_summaries, batch_size=5)
    intermediate_summaries = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        intermediate_summaries = list(executor.map(summarize_batch, batches))

    # Recursively summarize until small enough
    return generate_final_summary(intermediate_summaries)
