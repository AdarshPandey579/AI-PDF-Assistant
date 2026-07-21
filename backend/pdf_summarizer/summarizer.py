from config import client, MODEL
from .prompts import (
    SYSTEM_PROMPT,
    SUMMARY_PROMPT,
    BATCH_SUMMARY_PROMPT,
    FINAL_SUMMARY_PROMPT
)
from utils.batching import batch_items
from concurrent.futures import ThreadPoolExecutor


def summarize_chunk(chunk):
    prompt = SUMMARY_PROMPT.format(text=chunk.page_content)
    response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "system", "content": SYSTEM_PROMPT},
                          {"role": "user", "content": prompt},
                          ]
    )
    return response.choices[0].message.content
        


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
        response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "system", "content": SYSTEM_PROMPT},
                          {"role": "user", "content": prompt},
                          ]
        )
        return response.choices[0].message.content
    
    batches = batch_items(chunk_summaries, batch_size=5)
    intermediate_summaries = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        intermediate_summaries = list(executor.map(summarize_batch, batches))

    # Recursively summarize until small enough
    return generate_final_summary(intermediate_summaries)
