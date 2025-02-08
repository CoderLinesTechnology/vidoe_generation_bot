def extract_audio(video_path, output_path="audio.wav"):
    from moviepy.editor import VideoFileClip
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_path)
    return output_path

def clone_voice(audio_path, text):
    from TTS.api import TTS
    tts = TTS(model_name="tortoise", progress_bar=False, gpu=True)
    tts.tts_to_file(text=text, file_path="output_audio.wav", voice_dir="voices/", speaker_wav=audio_path)
    return "output_audio.wav"
