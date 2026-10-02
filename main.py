from telegram.ext import Application, CommandHandler
from config import Token
from handlers import start, help_command

app = Application.builder().token(Token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()