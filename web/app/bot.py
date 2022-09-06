import logging
import os

from telegram import Update, ForceReply
from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters, CallbackContext
)

from timer_bot import set_timer, unset

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.environ["TELEGRAM_API_TOKEN"]
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    """Sends explanation on how to use the bot."""
    update.message.reply_text("Hi! Use /set <seconds> to set a timer")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def hello() -> None:
    dispatcher.bot.send_message("Hello!")


def start_bot() -> None:
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    dispatcher.add_handler(CommandHandler("set", set_timer))
    dispatcher.add_handler(CommandHandler("unset", unset))

    updater.start_polling()
    # updater.idle()
