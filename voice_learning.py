# import logging

# logger = logging.getLogger(__name__)

def extract_audio(video_path, output_path="audio.wav"):
    try:
        from moviepy.editor import VideoFileClip
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_path)
        return output_path
    except Exception as e:
        # logger.error(f"Error in extract_audio: {e}", exc_info=True)
        raise

def clone_voice(audio_path, text):
    try:
        from TTS.api import TTS
        tts = TTS(model_name="tortoise", progress_bar=False, gpu=True)
        tts.tts_to_file(text=text, file_path="output_audio.wav", voice_dir="voices/", speaker_wav=audio_path)
        return "output_audio.wav"
    except Exception as e:
        # logger.error(f"Error in clone_voice: {e}", exc_info=True)
        raise