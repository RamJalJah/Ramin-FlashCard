import os
import csv
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Load flashcards from CSV
def load_flashcards(filename='pinyin_words.csv'):
    cards = []
    # Try different encodings
    encodings = ['utf-8-sig', 'utf-8', 'gb2312', 'gbk', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cards.append({'pinyin': row['pinyin'], 'english': row['english']})
            print(f"Successfully loaded {len(cards)} flashcards using {encoding} encoding")
            return cards
        except (UnicodeDecodeError, KeyError):
            cards = []
            continue
    
    raise Exception("Could not load CSV file with any supported encoding")
    return cards

# Global flashcards list
FLASHCARDS = load_flashcards()

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Pinyin Flashcard Bot! 🇨🇳\n\n"
        "Commands:\n"
        "/start - Show this message\n"
        "/practice - Start flashcard practice\n"
        "/stats - Show your statistics\n\n"
        "Let's practice your Chinese vocabulary!"
    )
    
    # Initialize user stats
    if 'seen' not in context.user_data:
        context.user_data['seen'] = 0
        context.user_data['revealed'] = 0

# Practice command - choose mode
async def practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📖 Pinyin → English", callback_data="mode_pinyin_to_english")],
        [InlineKeyboardButton("📝 English → Pinyin", callback_data="mode_english_to_pinyin")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Choose your practice mode:",
        reply_markup=reply_markup
    )

# Helper function to send next flashcard
async def send_next_card(chat_id, context: ContextTypes.DEFAULT_TYPE):
    # Pick a random flashcard
    card = random.choice(FLASHCARDS)
    context.user_data['current_card'] = card
    
    mode = context.user_data.get('mode', 'pinyin_to_english')
    
    if mode == 'pinyin_to_english':
        question = f"🎯 {card['pinyin']}"
        answer = card['english']
    else:  # english_to_pinyin
        question = f"🎯 {card['english']}"
        answer = card['pinyin']
    
    context.user_data['current_answer'] = answer
    
    # Create inline keyboard
    keyboard = [
        [InlineKeyboardButton("💡 Show Translation", callback_data="reveal")],
        [InlineKeyboardButton("➡️ Next Card", callback_data="next")],
        [InlineKeyboardButton("🛑 Stop Practice", callback_data="stop_practice")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"What does this mean?\n\n{question}",
        reply_markup=reply_markup
    )

# Handle button callbacks
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    # Handle mode selection
    if data.startswith("mode_"):
        mode = data.replace("mode_", "")
        context.user_data['mode'] = mode
        context.user_data['seen'] = 0
        context.user_data['revealed'] = 0
        
        mode_name = "Pinyin → English" if mode == "pinyin_to_english" else "English → Pinyin"
        await query.edit_message_text(f"Starting practice: {mode_name}\n\nGet ready! 🚀")
        await send_next_card(query.message.chat_id, context)
        return
    
    # Handle reveal translation
    if data == "reveal":
        context.user_data['revealed'] = context.user_data.get('revealed', 0) + 1
        context.user_data['seen'] = context.user_data.get('seen', 0) + 1
        
        mode = context.user_data.get('mode', 'pinyin_to_english')
        card = context.user_data['current_card']
        
        if mode == 'pinyin_to_english':
            question = card['pinyin']
            answer = card['english']
        else:
            question = card['english']
            answer = card['pinyin']
        
        seen = context.user_data['seen']
        revealed = context.user_data['revealed']
        remember_rate = ((seen - revealed) / seen * 100) if seen > 0 else 0
        
        response = (
            f"🎯 {question}\n\n"
            f"✅ Translation: {answer}\n\n"
            f"📊 Stats:\n"
            f"Cards seen: {seen}\n"
            f"Translations revealed: {revealed}\n"
            f"Remember rate: {remember_rate:.1f}%"
        )
        
        keyboard = [
            [InlineKeyboardButton("➡️ Next Card", callback_data="next")],
            [InlineKeyboardButton("🛑 Stop Practice", callback_data="stop_practice")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(response, reply_markup=reply_markup)
        return
    
    # Handle next card
    if data == "next":
        context.user_data['seen'] = context.user_data.get('seen', 0) + 1
        await query.edit_message_text("Moving to next card... ⏭️")
        await send_next_card(query.message.chat_id, context)
        return
    
    # Handle stop practice
    if data == "stop_practice":
        seen = context.user_data.get('seen', 0)
        revealed = context.user_data.get('revealed', 0)
        remember_rate = ((seen - revealed) / seen * 100) if seen > 0 else 0
        
        await query.edit_message_text(
            f"Practice session ended! 🎉\n\n"
            f"📊 Final Stats:\n"
            f"Cards seen: {seen}\n"
            f"Translations revealed: {revealed}\n"
            f"Cards you remembered: {seen - revealed}\n"
            f"Remember rate: {remember_rate:.1f}%\n\n"
            f"Great work! 加油! Use /practice to start again."
        )
        return

# Stats command
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    seen = context.user_data.get('seen', 0)
    revealed = context.user_data.get('revealed', 0)
    remember_rate = ((seen - revealed) / seen * 100) if seen > 0 else 0
    
    await update.message.reply_text(
        f"📊 Your Statistics:\n\n"
        f"Total cards seen: {seen}\n"
        f"Translations revealed: {revealed}\n"
        f"Cards you remembered: {seen - revealed}\n"
        f"Remember rate: {remember_rate:.1f}%\n\n"
        f"Keep practicing! 加油!"
    )

# Main function
def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '8479562697:AAF1aj7jYSzgyPvSjQFQOmo48OGooUKmxqY')
    
    # Create application
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("practice", practice))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # Start the bot
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()