# Video-to-Voice Bot with Facial Animation

This project uses machine learning and computer vision to extract facial landmarks from a video, animate a photo based on the facial movement in the video, and synthesize voice using the extracted audio. It then combines the animated photo with a cloned voice to generate a final video, which is sent to the user through a Telegram bot.

## Features

- Extracts facial landmarks from a video.
- Extracts and clones voice from the video.
- Animates a photo based on extracted facial landmarks.
- Synthesizes voice based on user input text.
- Combines the animated photo with the cloned voice to generate a video.
- Sends the final video to the user via a Telegram bot.

## Requirements

The following libraries are required to run the bot:

- `cv2` (OpenCV for video processing)
- `mediapipe` (For extracting facial landmarks)
- `ffmpeg-python` (For working with video files and audio)
- `moviepy` (For handling and processing video/audio files)
- `TTS` (For text-to-speech and voice cloning)
- `python-telegram-bot` (For handling Telegram bot commands)

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
