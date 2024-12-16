import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Вывод ошибок и информации о работе бота в консоль
# logging.basicConfig(
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#    level=logging.INFO
# )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {update.message.from_user.last_name}")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="К сожалению, я не знаю как это работает")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == "__main__":
    application = ApplicationBuilder().token('7266889222:AAGY1OSXxmdtzQ5tLWshnsNQberfMp9bhuU').build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(echo_handler)

    application.run_polling()
