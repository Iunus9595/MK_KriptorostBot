
import telebot
import time

bot = telebot.TeleBot("8163999640:AAGJ78lMs8Gxr0lYrG4qUBobCp1sClUV5m8")
channel_id = -1002533681792

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Бот запущен и работает в облаке.")
    time.sleep(3)
    bot.send_message(channel_id, "Сигнальный тест из облака: бот активен.")

bot.polling(none_stop=True)
