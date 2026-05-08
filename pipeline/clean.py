from pathlib import Path
import re
from config import UNCLEAN_MD_PATH, CLEAN_MD_PATH


def clean_md(input_path, output_path):
    p = Path(input_path)
    text = p.read_text()
    text = re.sub(r"\*\*==>.*?<==\*\*", "", text)  # images
    text = re.sub(r"<br\s*/?>", "", text)  # random <br> tags
    text = re.sub(r"\[[\d,;.:\s]+\]", "", text)  # references
    text = re.sub(r"CHAPTER 10.*", "", text, flags=re.DOTALL)  # Endnotes
    text = re.sub(
        r"\*\*----- Start of picture text -----\*\*.*?\*\*----- End of picture text -----\*\*",
        "",
        text,
        flags=re.DOTALL,
    )  # picture in the top right
    # md tables
    text = re.sub(r"(\|.+\|\n)+", "", text)
    text = re.sub(r"~~.*?~~", "", text)
    text = re.sub(r"^Source:.*$", "", text, flags=re.MULTILINE)  # captions
    text = re.sub(r"■", "", text)  # section end markers
    text = re.sub(
        r"^#{0,6}\s*Fi(?:gure|\b.*\bgure)\s+[A-Z0-9][-\w]*:.*$",
        "",
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )  # chart header attempt 1
    text = re.sub(
        r"^.+\s[a-z](\s[a-z])?\s*$", "", text, flags=re.MULTILINE
    )  # chart title attempt 2
    text = re.sub(
        r"^(CHAPTER\s+\d+)\s*\n#+\s*(.+)$",
        r"# \1 - \2",
        text,
        flags=re.MULTILINE,
    )  # Tidy chapter headers

    # standardising ## headers
    text = re.sub(
        r"^(CHAPTER\s+\d+)\s*\n#+\s*(.+)$",
        r"# \1 - \2",
        text,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^(CHAPTER\s+\d+)\s*\n+([A-Z][^\n]+)$",
        r"# \1 - \2",
        text,
        flags=re.MULTILINE,
    )

    Path(output_path).write_text(text)


if __name__ == "__main__":
    clean_md(UNCLEAN_MD_PATH, CLEAN_MD_PATH)

