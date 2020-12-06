import telebot

bot = telebot.TeleBot('499343415:AAHed_gG__Z95ti7zXovNfttOb40WGlKw_E')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Введи значение температуры используя только цифры, без специальных знаков, и я скажу что тебе лучше сегодня надеть:)')

@bot.message_handler(content_types=['text'])
def send_otv_temp(message):
    try:
        if int(message.text) >= 21:
            msg = bot.send_message(message.chat.id, 'Уф, сегодня жарковато, тебе лучше надеть футболку и шорты. Если хочешь, можешь искупаться)')
        elif int(message.text) >=10 and int(message.text) <= 20:
            msg = bot.send_message(message.chat.id, 'Я бы советовал тебе надеть свитер и штаны, чтобы не замерзнуть. Это будет самым правильным решением')
        elif int(message.text) >=0 and int(message.text) <= 9:
            msg = bot.send_message(message.chat.id, 'Сейчас лучше одеться потеплее, а то так и простудитсья можно. К примеру, можно надеть штаны, свитер и легкую куртку')
        elif int(message.text) >= -10 and int(message.text) <= 0:
            msg = bot.send_message(message.chat.id, 'Довольно холодно сегодня. Будь бы я человеком, я бы явно надел подштанники, штаны, свитер, шапку')
        elif int(message.text) <= -11:
            msg = bot.send_message(message.chat.id, 'Ой как холодно, мороз. Оденься как можно теплее, чтобы не заболеть. Как минимум подштанники, зимние ботинки, штаны, свитер и зимнюю куртку с шапкой. Еще желательно перчатки и шарф, чтобы уж точно не заболеть)')
    except:
        msg = bot.send_message(message.chat.id, 'Ты неправильно ввел значение температуры. Попробуй еще раз.')
bot.polling(none_stop=True)
