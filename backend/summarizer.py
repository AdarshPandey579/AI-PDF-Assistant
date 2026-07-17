from config import client, MODEL
from prompts import (
    SYSTEM_PROMPT,
    SUMMARY_PROMPT,
    FINAL_SUMMARY_PROMPT
)
from concurrent.futures import ThreadPoolExecutor

def summarize_chunk(chunk):
    prompt = SUMMARY_PROMPT.format(text=chunk.page_content)

    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def summarize_document(chunks):
    # return [summarize_chunk(chunk) for chunk in chunks]
    with ThreadPoolExecutor(max_workers=10) as executor:
        chunk_summaries = list(executor.map(summarize_chunk, chunks))

    return chunk_summaries


def generate_final_summary(chunk_summaries):
    combined_summary = "\n\n".join(chunk_summaries)
    prompt = FINAL_SUMMARY_PROMPT.format(text=combined_summary)

    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content