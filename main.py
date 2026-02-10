import telebot

TOKEN = '8350530854:AAEKz0KgAXNlxqAlbSomz3DTK_ulEXsHSfo'
MY_ID = 8001395458 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Бот активен! Жду вашу анкету.")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # Если пишет КТО-ТО ДРУГОЙ
    if message.chat.id != MY_ID:
        # Отправляем тебе уведомление
        info = f"🔔 **НОВАЯ АНКЕТА**\n👤 От: @{message.from_user.username}\n🆔 ID: {message.chat.id}\n\n📝 Текст:\n{message.text}"
        bot.send_message(MY_ID, info)
        # Отвечаем человеку
        bot.send_message(message.chat.id, "Ваше сообщение передано! ✅")
    
    # Если пишешь ТЫ
    else:
        if message.reply_to_message:
            try:
                # Пытаемся достать ID из сообщения, на которое ты отвечаешь
                user_id = message.reply_to_message.text.split("🆔 ID: ")[1].split("\n")[0].strip()
                bot.send_message(user_id, f"<b>Ответ от администратора:</b>\n\n{message.text}", parse_mode="HTML")
                bot.send_message(MY_ID, "✅ Ответ отправлен!")
            except:
                bot.send_message(MY_ID, "❌ Чтобы ответить, нажми 'Reply' на сообщение с ID!")
        else:
            bot.send_message(MY_ID, "Это ваш личный чат с ботом. Здесь вы будете получать анкеты.")

bot.polling(none_stop=True)
