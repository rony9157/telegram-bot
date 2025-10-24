"""
Telegram Bot without .env file
Author: ertre
"""

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# ===============================
# 🔹 এখানে সরাসরি তোমার টেলিগ্রাম বট টোকেন দাও
# ===============================
TOKEN = "8457159342:AAEikH__QQEhbOU45ylVUF6ws85vM8qG5WM"

# ===============================
# 🔸 এখানে প্রশ্ন ও উত্তর যোগ করো
# ===============================
QUESTIONS = {
    "🤔 এটা কী কাজ?": "Freecash এ মেইন যে কাজ তা হলো গ্যাম খেলে খেলে,লেভেল আপ করলে ওয়েবসাইট আমাদের পেমেন্ট করে,কিন্তু এতো পরিমাণ সময় ব্যায় করার এবং ধৈর্য কোনটাই আমাদের নেই..এছাড়া অনেকেই জানেন একসময় রুট ফোন,লাকি প্যাচার এবং গেইম গার্ডিয়ান এপ ব্যাবহার করে একসময় বিপুল পরিমানের অর্থ আয় করা সম্ভব হতো কিন্তু ওয়েব সিকিউরিটি এতো আপগ্রেড হয়েছে যে আগের সব মেথহোড এখন ব্যার্থ..তবে আমাদের কাছে এমন একটি হ্যাক এক্সটেনশন ফাইল আছে যা দিয়ে খুব সহজেই কোন সমস্যা ছাড়া গেম অফার হ্যাক বা লেভেল বাইপাস করা যায়,ফলে ওয়েবসাইট শুধু চেক করে গেম ঠিকমতো লেভেল আপ হয়েছে নাকি,আর আমাদের পেমেন্ট দিয়ে দেয়..",
    "💼 আমি কাজ করতে চাই": "IP, SSN, TOOLS আছে আপনার?",
    "🧭 কীভাবে শুরু করব?": "",
    # নিচে নতুন প্রশ্ন যোগ করতে পারবে 👇
    # "❓ নতুন প্রশ্ন এখানে লেখো": "",
}


# --- Command Handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(q)] for q in QUESTIONS.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "👋 স্বাগতম! নিচের প্রশ্নগুলোর যেকোনো একটি বেছে নাও 👇",
        reply_markup=reply_markup
    )


# --- Message Handler ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()

    if user_text in QUESTIONS:
        answer = QUESTIONS[user_text]
        if answer:
            await update.message.reply_text(answer)
        else:
            await update.message.reply_text("✍️ এই প্রশ্নের উত্তর এখনো সেট করা হয়নি।")
    else:
        await update.message.reply_text(
            "🤖 দুঃখিত, আমি বুঝতে পারিনি। দয়া করে নিচের বাটনগুলো ব্যবহার করো।"
        )


# --- Main Function ---
def main():
    if not TOKEN:
        raise ValueError("⚠️ TELEGRAM_BOT_TOKEN missing! Please set it above.")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running")
    app.run_polling()


if __name__ == "__main__":
    main()
