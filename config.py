
import os

class Config(object):
    BOT_USERNAME = os.environ.get("BOT_USERNAME",'link_Short_dagd_bot')
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", '')
    BOT_TOKEN = os.environ.get("BOT_TOEKEN", '')
    HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nI Am **PyTube Bot**.

I'm A Youtube Video Downloader Bot In High Resolution\nSend Me A link of Youtube And I will Send Your The Video Thank You. I Also have Support Channel ! Please Check **About Bot** Button.
"""
    ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Rudraa332

Developer is Excellent. And Learning from Official docs and ChatGpt. if you want to know about the developer the You can Dm Me.
I Am A Simple Quick learner Student if you want to teach me Please help Me to Improve myself.
[Rudraa](https://www.telegram.me/rudraa332) (Contect Me)
"""
    ABOUT_BOT_TEXT=f""" 

    I Am **Rudraa's** PyTube bot! \n I am simple youtube video Downloader bot. Send me a youtube link and I will give you th video of link!😊


    🤖 **My Name:** [Pytube Bot](https://t.me/{BOT_USERNAME})

    📝 **Language:** [Python3](https://www.python.org/)

    📚 **Library1:** [Pyrogram](https://docs.pyrogram.org/)

    📚 **Library2:** [PyTube](https://pypi.org/project/pytube/)

    📡 **Hosted on:** [Railway](https://render.com/)

    🧑🏻‍💻 **Developer:** @Rudraa332

    👥 **Support Group:** [Support Group](https://t.me/joint0t)

    📢 **Updates Channel:** [Bot Channel](https://t.me/bot_channelv1)
"""