import pytube
import os
from config import Config
from pyrogram import Client, filters, enums
from pyrogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)

# Create a Pyrogram client object

API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN
HOME_TEXT = Config.HOME_TEXT
ABOUT_DEV_TEXT = Config.ABOUT_DEV_TEXT
ABOUT_BOT_TEXT = Config.ABOUT_BOT_TEXT

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# Define a handler function to respond to /start command
@app.on_message(filters.command('start'))
def start_handler(client, message):
    message.reply_text(
        HOME_TEXT.format(message.from_user.first_name, message.from_user.id),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group 🥺", url="https://telegram.me/Joint0T"),
                    InlineKeyboardButton(
                        "Bots Channel 🙂", url="https://telegram.me/bot_channelv1")
                ],
                [
                    InlineKeyboardButton(
                        "About Bot", callback_data="aboutbot"),
                    InlineKeyboardButton(
                        "About Dev", callback_data="aboutdevs")
                ]
            ]
        )
    )

# Define a handler function to respond to text messages containing a YouTube link
# @app.on_message(filters.text & filters.private)
# async def youtube_handler(client, message: Message):


@app.on_message(filters.regex(".*(youtube.com/|youtu.be/).*") & filters.private)
async def handle_message(client, message: Message):
    # Create a YouTube object and get the highest resolution stream
    yt = pytube.YouTube(message.text)
    stream = yt.streams.get_highest_resolution()
    await app.send_chat_action(chat_id=message.chat.id, action=enums.ChatAction.TYPING)

    # Download the video to the current working directory
    file_path = stream.download()
    await app.send_chat_action(chat_id=message.chat.id, action=enums.ChatAction.RECORD_VIDEO)

    # Display a "sending video" message
    await app.send_chat_action(chat_id=message.chat.id, action=enums.ChatAction.UPLOAD_VIDEO)

    # Send the video file to the user
    video_file = await app.send_video(chat_id=message.chat.id, video=file_path, caption='Here is your video!')
    # await app.send_document(chat_id=message.chat.id, document=video_file.video.file_id)
    os.remove(file_path)
# Start the Pyrogram client


@app.on_callback_query()
async def button(client, cmd: CallbackQuery):
    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            ABOUT_DEV_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Get My Repo🙌",
                                             url="https://github.com/Rudraa332/Pytube-Telegram-Bot")
                    ],
                    [
                        InlineKeyboardButton(
                            "Go Home", callback_data="gotohome"),
                        InlineKeyboardButton(
                            "About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )

    elif "aboutdevs" in cb_data:
        await cmd.message.edit(
            ABOUT_DEV_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Get My Repo🙌",
                                             url="https://github.com/Rudraa332/Pytube-Telegram-Bot")
                    ],
                    [
                        InlineKeyboardButton(
                            "About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton(
                            "Go Home", callback_data="gotohome")
                    ]
                ]
            )
        )

    elif "gotohome" in cb_data:
        await cmd.message.edit(
            HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Support Group", url="https://telegram.me/Joint0T"),
                        InlineKeyboardButton(
                            "Bots Channel", url="https://telegram.me/bot_channelv1")
                    ],
                    [
                        InlineKeyboardButton(
                            "About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton(
                            "About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )

app.run()
