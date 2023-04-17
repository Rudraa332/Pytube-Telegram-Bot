import pytube 
import os
from pyrogram import Client, filters,enums
from pyrogram.types import Message 

# Create a Pyrogram client object
api_id = 9126459
api_hash = '238c912d48a9ec0d0e8b05738f358ffc'
bot_token = '5835101866:AAHxF8vWL20cEYxVWjRiULWtQ2RWLgQcYio'
app = Client('my_bot', api_id, api_hash, bot_token=bot_token)

# Define a handler function to respond to /start command
@app.on_message(filters.command('start'))
def start_handler(client, message):
    message.reply_text('Send me a YouTube link to download.')

# Define a handler function to respond to text messages containing a YouTube link
# @app.on_message(filters.text & filters.private)
# async def youtube_handler(client, message: Message):
@app.on_message(filters.regex(".*(youtube.com/|youtu.be/).*"))
async def handle_message(client, message: Message):
        # Create a YouTube object and get the highest resolution stream
        yt = pytube.YouTube(message.text)
        stream = yt.streams.get_highest_resolution()
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.TYPING)

        # Download the video to the current working directory
        file_path = stream.download()
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.RECORD_VIDEO)


        # Display a "sending video" message
        await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_VIDEO)

        # Send the video file to the user
        video_file = await app.send_video(chat_id=message.chat.id, video=file_path, caption='Here is your video!')
        # await app.send_document(chat_id=message.chat.id, document=video_file.video.file_id)
        os.remove(file_path)
# Start the Pyrogram client
app.run()
