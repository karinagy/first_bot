import telebot
from telebot import types  # для указание типов

token = '5293221845:AAG6B44cVULZtPIJUPGzOCMfVyurHYXm7mY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Прайс")
    btn2 = types.KeyboardButton("❓ Расскажи про комнаты")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот самого лучшего тусовочного места в Минске!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш инстаграм',
                                             url='https://instagram.com/ployka_minsk?utm_medium=copy_link')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди в наш инстаграмм за подробностями.",
                     reply_markup=markup)


@bot.message_handler(commands=['slivky'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Slivky',
                                             url='https://www.slivki.by/arenda-televizorov-komnat-minsk-skidka-ployka?utm_source=search_result&utm_medium=%D0%9F%D0%BB%D0%BE%D0%B9%D0%BA%D0%B0')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди для получения скидки при посещении.",
                     reply_markup=markup)


@bot.message_handler(content_types=['text', 'photo'])
def func(message, markup=None):
    if (message.text == "Прайс"):
        bot.send_message(message.chat.id, text="Стоимость услуг (60 мин):")
        bot.send_message(message.chat.id, text="- игра в PS4 в общем зале: 10 руб.,")
        bot.send_message(message.chat.id, text="- вип-комната <Жёлтая> (до 3 человек):20 руб.,")
        bot.send_message(message.chat.id, text="- вип-комната <Фиолетовая> (до 5 человек):18 руб.,")
        bot.send_message(message.chat.id, text="- вип-комната <Голубая> (до 7 человек):25 руб.,")
        bot.send_message(message.chat.id, text="- вип-комната <Коричневая> (до 10 человек):30 руб.,")
        bot.send_message(message.chat.id, text="- вип-комната <Серая> (до 10 человек): 45 руб." , reply_markup=markup)








    elif (message.text == "❓ Расскажи про комнаты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Голубая")
        btn2 = types.KeyboardButton("Желтая")
        btn3 = types.KeyboardButton("Фиолетовая")
        btn4 = types.KeyboardButton("Серая")
        btn5 = types.KeyboardButton("Коричневая")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Расскажи про комнаты", reply_markup=markup)

    elif message.text == "Голубая":
        bot.send_message(message.chat.id,
                         text="Голубая комната вмещает до 7 человек, включает большой диван, кресла мешки, большой телевизор на 55 дюймов, мощную аудиосистему и закрывается на ключ")
        img1 = "https://wampi.ru/image/RhIZ90E"
        bot.send_message(message.chat.id, text=img1)



    elif message.text == "Желтая":
        bot.send_message(message.chat.id,
                         text="Желтая комната комфортно вмещает до 3 человек, включает большой диван, мощную аудиосистему и закрывается на ключ")
        img2 = "https://wampi.ru/image/RhIjjIs"
        bot.send_message(message.chat.id, text=img2)



    elif message.text == "Фиолетовая":
        bot.send_message(message.chat.id,
                         text="Фиолетовая комната включает диван и кресло-мешок, вмещает до 5 человек и закрывается шторкой")
        img3 = "https://wampi.ru/image/RhIrsYn"
        bot.send_message(message.chat.id, text=img3)

    elif message.text == "Серая":
        bot.send_message(message.chat.id,
                         text="Серая комната вмещает до 10 человек, включает 2 больших дивана, кресла мешки, большой телевизор на 60 дюймов, мощную аудиосистему, систему домашнего кинотеатра для объёмного звука при игре в PS/просмотре фильмов и закрывается на ключ")
        bot.send_message(message.chat.id,
                         text="https://wampi.ru/image/RhIrJBq")

    elif message.text == "Коричневая":
        bot.send_message(message.chat.id,
                         text="Коричневая комната вмещает до 10 человек, включает большой диван, кресла мешки, большой телевизор на 55 дюймов, мощную аудиосистему и закрывается на ключ")
        bot.send_message(message.chat.id,
                         text="https://wampi.ru/image/RhIr0mw")


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Прайс")
        button2 = types.KeyboardButton("❓ Расскажи про комнаты")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


bot.polling(none_stop=True)
