import kokoro
import soundfile as sf
from config import TTS_OUTPUT, CLEAN_MD_PATH


def tts_loop(text):
    pipeline = kokoro.KPipeline(lang_code="b")
    generator = pipeline(text, voice="bf_emma", speed=1, split_pattern=r"\n")
    total_chunks = len(text.split("\n"))

    for i, (_, _, audio) in enumerate(generator):
        sf.write(TTS_OUTPUT / f"{i}.wav", audio, 24000)
        print(f"Progress - tts performed on {i + 1} / {total_chunks} lines")


if __name__ == "__main__":
    text = CLEAN_MD_PATH.read_text()
    tts_loop(text)
