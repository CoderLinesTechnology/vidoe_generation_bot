import subprocess

def combine_audio_video(video_path, audio_path, output_path="output.mp4"):
    cmd = f"ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental {output_path}"
    subprocess.run(cmd, shell=True, check=True)
    return output_path