import telebot
from telebot import types  # для указание типов

token = '5293221845:AAG6B44cVULZtPIJUPGzOCMfVyurHYXm7mY'
bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup(True)

#Три главные кнопки бота

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Прайс")
    btn2 = types.KeyboardButton("❓ Расскажи про комнаты")
    btn3 = types.KeyboardButton("📅 Забронировать комнату")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот самого лучшего тусовочного места в Минске!".format(
                         message.from_user), reply_markup=markup)

#Кнопка с ссылкой инстаграмма

@bot.message_handler(commands=['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Наш инстаграм',
                                             url='https://instagram.com/ployka_minsk?utm_medium=copy_link')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди в наш инстаграмм за подробностями.",
                     reply_markup=markup)


#Кнрпка с ссылкой на сливки(купон на скидку)

@bot.message_handler(commands=['slivky'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='Slivky',
                                             url='https://www.slivki.by/arenda-televizorov-komnat-minsk-skidka-ployka?utm_source=search_result&utm_medium=%D0%9F%D0%BB%D0%BE%D0%B9%D0%BA%D0%B0')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди для получения скидки при посещении.",
                     reply_markup=markup)


#Первая главная кнопка выводит прайс комнат

name_of_person = ''

age = 0


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

#Вторая главная кнопка дает начало еще 6 кнопкам(5 комнат+ возможность вернуться в начало)

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
        button3 = types.KeyboardButton("📅 Забронировать комнату")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
 
        
        
    elif message.text == "📅 Забронировать комнату":
        name = bot.send_message(message.from_user.id, 'Введите ваше имя для бронирования комнаты: ',
                                reply_markup=keyboard)

        bot.register_next_step_handler(name, get_age)
    else:
        bot.send_message(message.chat.id, text='Упс.Такой команды я не знаю.')


def get_age(message):
    global name_of_person
    age_of = bot.send_message(message.chat.id, text='Введите ваш возраст')
    name_of_person = message.text

    bot.register_next_step_handler(age_of, get_telephone)


def get_telephone(message):
    global age
    age = int(message.text)
    if age < 18:
        bot.send_message(message.chat.id,
                         text='‼️Уважаемые посетители плойки! Информируем вас о том, что в связи с законодательством РБ на территории заведения несовершенолетним запрещается:распивать и приобретать алкогольные напитки, курить кальян, а так же приобретать HQD у администратора.Спасибо за понимание! ‼️')
    else:
        bot.send_message(message.chat.id,
                         text='✅️Уважаемые посетители плойки!Спешим информировать вас о том, что на территории нашего заведения вы всегда можете заказать кальян, а так же приобрести алкогольные напитки.С уважением, администация плойки! ✅')
    tel = bot.send_message(message.chat.id,
                           text='Введите номер телефона, для завершения брони', reply_markup=keyboard)
    bot.register_next_step_handler(tel, confirm_booking)

#Прозрачные кнопки для подтверждения брони

def confirm_booking(message):
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = f'Ваше имя {name_of_person} и Ваш номер телефона {message.text}.Верно ли указана вся информация?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    
#Реакция на нажатие кнопок

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "yes":
            bot.send_message(call.message.chat.id,
                             text='Бронь передана , в ближайшее время с вами свяжется администатор для подтверждения брони')
        elif call.data == "no":
            error = bot.send_message(call.message.chat.id,
                                     text='Если возникла ошибка при бронировании, следует повторить операцию бронирования сначала')


bot.polling(none_stop=True)
