import kokoro
import soundfile as sf
from config import TTS_OUTPUT, CLEAN_MD_PATH
import time
from datetime import datetime


def tts_loop(md_path, chunk_path):
    text = md_path.read_text()
    pipeline = kokoro.KPipeline(lang_code="b")
    generator = pipeline(text, voice="bf_emma", speed=1, split_pattern=r"\n")
    total_chunks = len(text.split("\n"))

    start = time.time()

    for i, (_, _, audio) in enumerate(generator):
        sf.write(chunk_path / f"{i + 1:05d}.wav", audio, 24000)
        elapsed = time.time() - start
        rate = elapsed / (i + 1)
        eta = time.time() + rate * (total_chunks - (i + 1))
        eta_readable = datetime.fromtimestamp(eta).strftime("%H:%M:%S")
        print(f"TTS performed on {i + 1} / {total_chunks} lines")
        print(f"Average rate - {rate:.3f} per line")
        print(f"ETA - {eta_readable}")
        print("=================================================")


if __name__ == "__main__":
    tts_loop(CLEAN_MD_PATH, TTS_OUTPUT)
