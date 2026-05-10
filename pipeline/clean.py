from pathlib import Path
import re
from config import UNCLEAN_MD_PATH, CLEAN_MD_PATH


def clean_md(input_path, output_path):
    p = Path(input_path)
    text = p.read_text()

    # --- STRUCTURAL CLEANING ---
    text = re.sub(r"\*\*==>.*?<==\*\*", "", text)  # images
    text = re.sub(r"<br\s*/?>", "", text)  # random <br> tags
    text = re.sub(r"\[[\d,;.:\s]+\]", "", text)  # references
    text = re.sub(r"CHAPTER 10.*", "", text, flags=re.DOTALL)  # drop appendices
    text = re.sub(
        r"\*\*----- Start of picture text -----\*\*.*?\*\*----- End of picture text -----\*\*",
        "",
        text,
        flags=re.DOTALL,
    )  # picture callout boxes
    text = re.sub(r"(\|.+\|\n)+", "", text)  # markdown tables
    text = re.sub(r"~~.*?~~", "", text)  # strikethrough artifacts
    text = re.sub(r"^Source:.*$", "", text, flags=re.MULTILINE)  # orphaned captions
    text = re.sub(r"■", "", text)  # section end markers
    text = re.sub(
        r"^#{0,6}\s*Fi(?:gure|\b[^:]*?g?ure)\s+[A-Z0-9][-\w]*:.*$",
        "",
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )  # figure/chart titles including garbled variants

    # Chapter header normalisation
    text = re.sub(
        r"^(CHAPTER\s+\d+)\s*\n#+\s*(.+)$",
        r"# \1 - \2",
        text,
        flags=re.MULTILINE,
    )  # Ch 4-6: CHAPTER N + markdown heading
    text = re.sub(
        r"^(CHAPTER\s+\d+)\s*\n+([A-Z][^\n]+)$",
        r"# \1 - \2",
        text,
        flags=re.MULTILINE,
    )  # Ch 7-9: CHAPTER N + plain text title

    # Specific noise lines
    text = re.sub(
        r"^#{1,6}\s*(Contents|In this assessment[^\n]*)\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )  # empty/useless headings
    text = re.sub(
        r"^(Board of Directors|IOM Trust|IOM 2006 Company)\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )  # isolated diagram labels (plain)
    text = re.sub(
        r"^## Board of Directors\s*$", "", text, flags=re.MULTILINE
    )  # headed variant
    text = re.sub(
        r"^Legal Entity Type Money Laundering Rating.*$",
        "",
        text,
        flags=re.MULTILINE,
    )  # pipeless table remnant
    text = re.sub(
        r"^When Established and Jurisdiction of Governance\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )  # orphaned caption
    text = re.sub(
        r"^#{0,6}\s*by Occurrence as a Percentage\s*$",
        "",
        text,
        flags=re.MULTILINE,
    )  # truncated heading fragment

    # Duplicate paragraph removal
    text = text.replace(
        'Most recorded ML offences (81%) are domestic, commonly 50% of predicated by drug offending, although less than the proceeds are related to drugs. Internationally, the most common predicate offence is fraud, with investigations being complex, having much higher values and much greater economic and international impact."',
        "",
        1,
    )  # remove first (garbled) occurrence
    marker = "The Island must also recognise that its attractiveness as a financial centre depends on maintaining high standards of governance and compliance."
    first = text.find(marker)
    if first != -1:
        second = text.find(marker, first + 1)
        if second != -1:
            end = text.find("\n\n", second)
            text = text[:second] + text[end:]  # remove second occurrence

    # --- TTS NORMALISATION ---
    text = re.sub(r"^[-●•\*]\s+", "", text, flags=re.MULTILINE)  # strip bullet markers
    text = re.sub(r"(^#{1,6}[^\n]*)\n", r"\1HEADINGBREAK", text, flags=re.MULTILINE)
    text = re.sub(r"\n+([^#\n])", r" \1", text)  # flatten prose newlines
    text = text.replace("HEADINGBREAK", "\n")  # restore heading line endings
    text = re.sub(r"([.!?])\s+(?=[A-Z])", r"\1\n", text)  # one sentence per line
    text = re.sub(r" +", " ", text)  # collapse multiple spaces
    text = re.sub(r" +$", "", text, flags=re.MULTILINE)  # strip trailing spaces
    text = re.sub(r"\n+", "\n", text)  # collapse empty lines
    text = re.sub(
        r"^#{1,6}\s*\d+\.\s*\n", "", text, flags=re.MULTILINE
    )  # stray chapter heads
    text = re.sub(r"^ +", "", text, flags=re.MULTILINE)  # " " leading lines
    text = re.sub(r"^#{0,6}\s*Com anies Re istr.*\n", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^Risk Assessments of Domestic Le al.*\n", "", text, flags=re.MULTILINE
    )
    text = re.sub(r"^Percenta e for TCSP.*\n", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^#{1,6}\s*with Companies Registry.*\n", "", text, flags=re.MULTILINE
    )
    text = re.sub(r"^## EASE AND SPEED OF\s*\n", "", text, flags=re.MULTILINE)
    text = re.sub(
        r"^## A Registered Agent is not required\.\s*\n", "", text, flags=re.MULTILINE
    )
    text = re.sub(r"^#{1,6}\s*●\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

    Path(output_path).write_text(text)


if __name__ == "__main__":
    clean_md(UNCLEAN_MD_PATH, CLEAN_MD_PATH)
