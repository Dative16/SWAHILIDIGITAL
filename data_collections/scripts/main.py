from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import os


def convert_video_to_audio(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    video.close()


def split_audio(audio_path, output_folder, clip_length=10):
    audio = AudioSegment.from_wav(audio_path)
    duration = len(audio)  # Duration in milliseconds
    num_clips = duration // (clip_length * 1000)  # Calculate the number of 10-second clips

    for i in range(num_clips):
        start_time = i * clip_length * 1000
        end_time = start_time + clip_length * 1000
        clip = audio[start_time:end_time]
        clip.export(os.path.join(output_folder, f"clip_{i + 1}.wav"), format="wav")



video_path = "videoplayback_27.mp4"
output_audio_path = "output_audio.wav"
output_folder = "audio_clips"

# Convert video to audio
convert_video_to_audio(video_path, output_audio_path)

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Split the audio into 10-second clips
split_audio(output_audio_path, output_folder)
