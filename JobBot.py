from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import pandas as pd
import os

TOKEN = '7869911210:AAFz5_DlNf047oBulj_LfU6ykjYlMI0KhKI'

# Create an Excel file if it doesn't exist
if not os.path.exists('user_ids.xlsx'):
    pd.DataFrame(columns=['User ID']).to_excel('user_ids.xlsx', index=False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        # Save the user ID to the Excel file
        user_ids_df = pd.read_excel('user_ids.xlsx')
        new_row = pd.DataFrame([{'User ID': user_id}])
        user_ids_df = pd.concat([user_ids_df, new_row])
        user_ids_df.to_excel('user_ids.xlsx', index=False)

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I hope you're doing well! I noticed you are interested in IT jobs. Join my Telegram channel, https://t.me/joblistings_offcampus, where we share curated job listings tailored to your interests. We are committed to helping you find your ideal job.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

async def custom_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        custom_message = "Hello! I hope you're doing well! I noticed you are interested in IT jobs. Join my Telegram channel, https://t.me/joblistings_offcampus, where we share curated job listings tailored to your interests. We are committed to helping you find your ideal job."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=custom_message)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    custom_response_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, custom_response)

    application.add_handler(start_handler)
    application.add_handler(custom_response_handler)

    application.run_polling()

if __name__ == '__main__':
    main()