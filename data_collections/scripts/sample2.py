import librosa
import numpy as np
import soundfile as sf


def reduce_noise(wav_file, output_file, noise_reduction_factor=0.5):
    y, sr = librosa.load(wav_file)

    # Separate harmonic (speech) and percussive (background music) components
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    # Reduce the percussive component
    y = y_harmonic + noise_reduction_factor * y_percussive

    # Save the output
    sf.write(output_file, y, sr)



wav_file = "clip_2.wav"
output_file = "cleaned_audio.wav"
reduce_noise(wav_file, output_file)
