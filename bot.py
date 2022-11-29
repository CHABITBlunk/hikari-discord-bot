import lightbulb, hikari
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = str(os.getenv("TOKEN"))

bot = lightbulb.BotApp(token=TOKEN, default_enabled_guilds=(856408164793450506))

bot.load_extensions_from('./extensions')

bot.run()

