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
- Keep the summary concise.
- Use bullet points.
- Preserve names, dates, and numbers.
- Maximum 100 words.

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
You are an expert technical document summarizer.
Your task is to merge multiple section summaries into one accurate, concise and information-rich final summary.

Requirements:
- Maximum 500 words.
- Preserve the document's main purpose and key conclusions.
- Merge duplicated information into one coherent point.
- Compress explanations rather than factual information.
- Never remove important names, versions, dates, numbers,
  statistics, model names or table values.
- Preserve important headings when useful.
- Summarize tables by describing their key information.
- Preserve important bullet points.
- Mention code snippets only when they help explain the document.
- Never hallucinate or invent information.
- Write clear professional Markdown.

Use only headings that are relevant to the document.
Suggested headings:
# Overview
# Key Concepts
# Important Details
# Timeline (if applicable)
# Models / Tables (if applicable)
# Conclusion

Section Summaries:
{text}
"""