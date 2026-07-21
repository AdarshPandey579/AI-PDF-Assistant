SYSTEM_PROMPT = """
You are an expert PDF document summarizer.

Your job is to:
- Read the provided text carefully.
- Identify the main ideas.
- Ignore unnecessary details.
- Produce clear and concise summaries.
- Never make up information that is not present in the text.
"""


SUMMARY_PROMPT = """
Summarize the following text.

Requirements:
- Summarize the main ideas and important information in this section.
- Keep only information essential to understanding this section.
- Remove repeated information.
- Omit boilerplate text, legal notices, contact information, navigation text, advertisements, and standard policies unless they are central to this section.
- Preserve names, dates, numbers, values, and other facts only when they are important to the meaning.
- If this section lacks sufficient context, summarize only what is explicitly stated without making assumptions about the rest of the document.
- Never invent information.
- Maximum 150 words.
- Use concise Markdown bullet points.

Text:
{text}
"""


BATCH_SUMMARY_PROMPT = """
Below are summaries from different sections of a document.
Your task is to merge them into a single concise summary.

Requirements:
- Remove duplicate information.
- Preserve important facts, names, dates, and numbers.
- Keep the result under 200 words.
- Use Markdown bullet points.

Summaries:
{text}
"""


FINAL_SUMMARY_PROMPT = """
Merge the section summaries into one clear, concise, and coherent final summary.

Requirements:
- Begin with a brief overview of what the document is about.
- Remove duplicate or repeated information.
- Keep only information that is essential to understand or use the document.
- Preserve key facts, names, dates, figures, conclusions, and other important details when they contribute to the document's meaning.
- Ignore repeated headers, footers, page numbers, legal notices, disclaimers, contact information, navigation text, advertisements, and other boilerplate unless they are central to the document.
- For structured documents (such as tickets, invoices, receipts, certificates, or forms), summarize the key fields instead of rewriting all content.
- Use headings only when they naturally improve readability.
- Use concise Markdown.
- Maximum 250 words.
- Never invent or infer information that is not present.

Section Summaries:
{text}
"""