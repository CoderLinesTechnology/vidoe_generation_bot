from telegram.ext import Application, CommandHandler, MessageHandler, filters
import asyncio
import os
import sys

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

async def process_video(video_path, chat_id):
    # Extract voice and train/model
    audio_path = extract_audio(video_path)
    # Extract facial landmarks
    landmarks = extract_facial_landmarks(video_path)
    # Save data to user session (e.g., Redis)
    store_user_data(chat_id, audio_path, landmarks)

async def generate_video(photo_path, text, chat_id):
    # Retrieve user data
    audio_path, landmarks = get_user_data(chat_id)
    # Synthesize voice
    cloned_audio = clone_voice(audio_path, text)
    # Animate photo
    output_video = animate_photo(photo_path, landmarks)
    # Combine audio and video
    final_video = combine_audio_video(output_video, cloned_audio)
    # Send to user
    await app.bot.send_video(chat_id, final_video)



async def start(update, context):
    await update.message.reply_text("Upload a video for voice/facial learning.")
    
async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = await update.message.video.get_file()
    await video.download_to_drive("user_video.mp4")
    asyncio.create_task(process_video("user_video.mp4", update.message.chat_id))
    await update.message.reply_text("Processing video... Upload a photo next.")
  
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = await update.message.photo[-1].get_file()
    await photo.download_to_drive("user_photo.jpg")
    await update.message.reply_text("Photo received. Type the message to synthesize.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    asyncio.create_task(generate_video("user_photo.jpg", text, update.message.chat_id))
    await update.message.reply_text("Generating video...")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))
    app.run_polling()

if __name__ == "__main__":
    main()