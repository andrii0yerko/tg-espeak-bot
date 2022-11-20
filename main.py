import logging
import os
from html import escape
from uuid import uuid4

from telegram import InlineQueryResultCachedVoice, Update
from telegram.ext import Application, ContextTypes, InlineQueryHandler

from espeak_bot.espeak import voice

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TG_BOT_TOKEN")
BUFFER = os.environ.get("TG_BUFFER_CHAT_ID")


async def upload_voice(audio):
    msg = await application.bot.send_voice(BUFFER, audio)
    return msg.voice.file_id


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if query.strip() == "":
        return

    audio = voice(escape(query))

    results = [
        InlineQueryResultCachedVoice(
            id=str(uuid4()),
            voice_file_id=await upload_voice(audio),
            title="Voice out",
        ),
    ]

    await update.inline_query.answer(results)


if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    application.add_handler(InlineQueryHandler(inline_query))

    application.run_polling()
