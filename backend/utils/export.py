from pathlib import Path

EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)


def save_markdown(summary: str) -> str:
    file_path = EXPORT_DIR / "summary.md"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(summary)

    return str(file_path)