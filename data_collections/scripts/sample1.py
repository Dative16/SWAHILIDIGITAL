import os
from pydub import AudioSegment


def convert_all_mp3_to_wav(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            mp3_file = os.path.join(input_folder, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_file = os.path.join(output_folder, wav_filename)

            # Convert MP3 to WAV
            audio = AudioSegment.from_mp3(mp3_file)
            audio.export(wav_file, format="wav")
            print(f"Converted {mp3_file} to {wav_file}")


# usage
input_folder = "58"  # input folder
output_folder = "uot_folder"  # output folder

convert_all_mp3_to_wav(input_folder, output_folder)
