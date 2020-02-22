import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот придуманный для того чтобы отправлять уведомления в основном по учёбе (пары,дз и прочее). Пока что я не работаю. Жди чуда.".format(message.from_user, bot.get_me()),
        parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Ты думал тебе тут помогут? Не не не, чувак. Закрывай телеграм иди нахуй.".format(message.from_user, bot.get_me()),
        parse_mode='html')       


#@bot.message_handler(content_types=['text'])
#def lalala(message):
#    bot.send_message(message.chat.id, message.text)

# RUN
bot.polling(none_stop=True)