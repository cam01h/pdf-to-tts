from pathlib import Path

# File Paths
PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MD_DIR = OUTPUT_DIR / "md"
UNCLEAN_MD_PATH = MD_DIR / "unclean.md"
CLEAN_MD_PATH = MD_DIR / "clean.md"
AUDIO_DIR = OUTPUT_DIR / "audio"
TTS_OUTPUT = AUDIO_DIR / "tts_chunks"
