from pathlib import Path

# Config variables
EXTRACTION_MARGINS = (0, 50, 0, 50)

# File Paths
PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MD_DIR = OUTPUT_DIR / "md"
UNCLEAN_MD_PATH = MD_DIR / "unclean.md"
CLEAN_MD_PATH = MD_DIR / "clean.md"
