from pathlib import Path
from pydub import AudioSegment
from config import TTS_OUTPUT, FINAL_OUTPUT


def stitch(wav_chunks_path, output_path):
    wav_list = sorted(Path(wav_chunks_path).glob("*.wav"))
    num_wavs = len(wav_list)

    audio = AudioSegment.silent(duration=1000)  # 1 sec of silence at the start
    sentence_break = AudioSegment.silent(duration=300)

    print("Stitching .wav files")
    for i, f in enumerate(wav_list):
        audio += AudioSegment.from_wav(f)
        audio += sentence_break
        print(f"Files stitched - {i + 1} / {num_wavs}")

    audio.export(Path(output_path) / "final.mp3", format="mp3")
    print("Stitching complete")


if __name__ == "__main__":
    stitch(TTS_OUTPUT, FINAL_OUTPUT)
