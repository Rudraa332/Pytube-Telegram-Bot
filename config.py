
import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", ' ')
    BOT_TOKEN = os.environ.get("BOT_TOEKEN", '')
    HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nI Am **PyTube Bot**.

I'm A Youtube Video Downloader Bot In High Resolution\nSend Me A link of Youtube And I will Send Your The Video Thank You. I Also have Support Channel ! Please Check **About Bot** Button.
"""