from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً بك في بوت دفترة!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أنا بوت دعم فني لشركة دفترة.\nاكتب /start عشان تبدأ")

def main():
    from dotenv import load_dotenv
    load_dotenv()
    import os
    
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    application.run_polling()

if __name__ == "__main__":
    main()