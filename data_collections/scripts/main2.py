from pydub import AudioSegment
import librosa
import numpy as np
import soundfile as sf


def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")


def reduce_noise(wav_file, output_file, noise_reduction_factor=0.5):
    y, sr = librosa.load(wav_file)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    y = y_harmonic + noise_reduction_factor * y_percussive
    sf.write(output_file, y, sr)


# Example usage
mp3_file = "input_audio.mp3"
wav_file = "output_audio.wav"
cleaned_file = "cleaned_audio.wav"

convert_mp3_to_wav(mp3_file, wav_file)
reduce_noise(wav_file, cleaned_file)
