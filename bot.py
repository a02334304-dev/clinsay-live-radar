import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 CLINSAY LIVE RADAR запущен!\n"
        "Цель: @clinsay\n"
        "Режим: Standoff 2\n\n"
        "Команды:\n"
        "/status — статус помощника"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📡 CLINSAY RADAR работает!\n"
        "Автоматическое наблюдение за LIVE пока не подключено."
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("status", status))

app.run_polling()
