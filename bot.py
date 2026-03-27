import telebot, os
from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin
from bot_logic import get_duck_image_url


bot = telebot.TeleBot('TOKEN')
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['random'])
def random(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['emoji'])
def emoji(message):
    bot.reply_to(message, gen_emodji())

@bot.message_handler(commands=['coin'])
def coin(message):
    bot.reply_to(message, flip_coin())

@bot.message_handler(commands=["photo"])
def photo(message):
    with open(r"images\mem1.png", "rb") as file:
        bot.send_photo(message.chat.id, file)




@bot.message_handler(commands=["info"])
def info(message):
    with open(r"bot\info.txt", "r", encoding="utf-8") as file2:
        content = file2.read()
        bot.reply_to(message, content)
#рецепт борща




@bot.message_handler(commands=["photo2"])
def photo(message):
    for izo in os.listdir("images"):
        with open(f"images\{izo}", "rb") as file:
            bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
