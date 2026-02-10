import telebot

TOKEN = '8350530854:AAEKz0KgAXNlxqAlbSomz3DTK_ulEXsHSfo'
MY_ID = 8001395458  # Твой ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Пришлите вашу анкету и юз.")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # Если пишет КТО-ТО ДРУГОЙ (не ты)
    if message.chat.id != MY_ID:
        info = f"🔔 **НОВАЯ АНКЕТА**\n👤 От: @{message.from_user.username}\n🆔 ID: {message.chat.id}\n\n📝 Текст:\n{message.text}"
        bot.send_message(MY_ID, info)
        bot.send_message(message.chat.id, "Ваше сообщение передано! ✅")
    
    # Если пишешь ТЫ ответом на сообщение
    elif message.reply_to_message:
        try:
            reply_text = message.reply_to_message.text
            user_id = reply_text.split("🆔 ID: ")[1].split("\n")[0].strip()
            bot.send_message(user_id, f"<b>Ответ от администратора:</b>\n\n{message.text}", parse_mode="HTML")
            bot.send_message(MY_ID, "✅ Ответ отправлен!")
        except:
            bot.send_message(MY_ID, "❌ Ошибка: ответьте на сообщение, где есть ID!")

bot.polling(none_stop=True)
