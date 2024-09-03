from pydub import AudioSegment
import os
from tqdm import tqdm


def convert_mp3_to_wav(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all mp3 files in the input folder
    for filename in tqdm(os.listdir(input_folder)):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(input_folder, filename)
            wav_filename = filename.replace(".mp3", ".wav")
            wav_path = os.path.join(output_folder, wav_filename)

            # Convert mp3 to wav
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")
            print(f"Converted {filename} to {wav_filename}")


def split_wav_to_clips(wav_folder, output_folder, clip_length=10 * 1000):  # 10 seconds in milliseconds
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all wav files in the folder
    for filename in tqdm(os.listdir(wav_folder)):
        if filename.endswith(".wav"):
            wav_path = os.path.join(wav_folder, filename)
            audio = AudioSegment.from_wav(wav_path)
            total_length = len(audio)

            for i in range(0, total_length, clip_length):
                clip = audio[i:i + clip_length]
                clip_filename = f"{filename.replace('.wav', '')}_clip_{i // clip_length + 1}.wav"
                clip_output_path = os.path.join(output_folder, clip_filename)
                clip.export(clip_output_path, format="wav")
                print(f"Created clip: {clip_filename}")


input_folder = 'audios'  # Folder containing mp3 files
wav_output_folder = 'wav_files'  # Folder to save wav files
clips_output_folder = 'clips'  # Folder to save 10-second clips

# Convert mp3 to wav
convert_mp3_to_wav(input_folder, wav_output_folder)

# Split wav files into 10-second clips
split_wav_to_clips(wav_output_folder, clips_output_folder)
