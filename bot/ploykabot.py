import telebot
from telebot import types  # для указание типов

token = '5293221845:AAG6B44cVULZtPIJUPGzOCMfVyurHYXm7mY'
bot = telebot.TeleBot(token)
keyboard = telebot.types.ReplyKeyboardMarkup(True)


# Главные 4 кнопки
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("📅 Забронировать комнату")
    markup.row(btn1)
    btn2 = types.KeyboardButton("❓ Расскажи про комнаты")
    markup.row(btn2)
    btn3 = types.KeyboardButton("✅ Прайс")
    btn4 = types.KeyboardButton("🥂 Ployka Бар")
    markup.row(btn3, btn4)
    btn5 = types.KeyboardButton("Сообщить о проблеме")
    markup.row(btn5)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот самого лучшего тусовочного места в Минске!Чем я могу тебе "
                          "помочь?".format(message.from_user), reply_markup=markup)


# Кнопка с ссылкой на инстаграм
@bot.message_handler(commands=['inst'])
def inst(message):
    markup = types.InlineKeyboardMarkup()
    btn_instagram = types.InlineKeyboardButton(text='Наш инстаграм',
                                               url='https://instagram.com/ployka_minsk?utm_medium=copy_link')
    markup.add(btn_instagram)
    bot.send_message(message.chat.id, text="Нажми на кнопку и перейди в наш инстаграмм за подробностями.",
                     reply_markup=markup)


# Кнопка с ссылкой на тикток
@bot.message_handler(commands=['slivky'])
def slivky(message):
    markup = types.InlineKeyboardMarkup()
    btn_slivky = types.InlineKeyboardButton(text='Купон на скидку',
                                            url='https://www.slivki.by/arenda-televizorov-komnat-minsk-skidka-ployka'
                                                '?utm_source=search_result&utm_medium=%D0%9F%D0%BB%D0%BE%D0%B9%D0%BA'
                                                '%D0%B0')
    markup.add(btn_slivky)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди по ссылке для получения скидки при посещении Ployka.",
                     reply_markup=markup)


# Кнопка с ссылкой на Яндекс Отзывы
@bot.message_handler(commands=['feedback'])
def feedback(message):
    markup = types.InlineKeyboardMarkup()
    btn_feedback = types.InlineKeyboardButton(text='Оставить отзыв',
                                              url='https://yandex.by/maps/org/ployka/64100616480/reviews/?ll=27'
                                                  '.573653%2C53.890893&z=18')
    markup.add(btn_feedback)
    bot.send_message(message.chat.id, "Нам важно ваше мнение!Перейдите по ссылке, чтобы оставить отзыв.",
                     reply_markup=markup)


# Кнопка с ссылкой на тикток
@bot.message_handler(commands=['tiktok'])
def tiktok(message):
    markup = types.InlineKeyboardMarkup()
    btn_tiktok = types.InlineKeyboardButton(text='Наш TikTok',
                                            url='https://vm.tiktok.com/ZMLj1L92X/')
    markup.add(btn_tiktok)
    bot.send_message(message.chat.id, "Переходи в наш TikTok и узнавай о скидках первым!",
                     reply_markup=markup)


name_of_person = ''
rooms = ''
age = 0
tel_of_person = 0
telephone = 0
TO_CHAT_ID = 957891234  # ID будущего администратора


# При нажатии на кнопку прайс , появляется текст с прайсом услуг
@bot.message_handler(content_types=['text', 'photo'])
def func(message):
    if message.text == "✅ Прайс":
        bot.send_message(message.chat.id,
                         text="Стоимость услуг (60 мин) :\n\n- игра в PS4 в общем зале\n*10 руб.*\n\n- вип-комната "
                              "💛Жёлтая💛 ( "
                              "до 3 человек)\n*20 руб.*\n\n- вип-комната 💜Фиолетовая💜 (до 5 человек)\n*18 "
                              "руб.*\n\n- вип-комната "
                              "💙Голубая💙 (до 7 человек)\n*25 руб.*\n\n- вип-комната 🤎Коричневая🤎 (до 10 человек)\n*30 "
                              "руб.*\n\n- вип-комната 🤍Серая🤍 (до 10 человек)\n*45 руб.*", parse_mode='Markdown')
    elif message.text == "🥂 Ployka Бар":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        alcoh = types.KeyboardButton("Алкогольные напитки")
        drink = types.KeyboardButton("Напитки")
        snack = types.KeyboardButton("Снэки")
        hookah = types.KeyboardButton("Кальян")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(alcoh, drink, snack, hookah, back)
        bot.send_message(message.chat.id, text="Выбери интересующий раздел Ployka Бара", reply_markup=markup)

    elif message.text == "Алкогольные напитки":
        bot.send_message(message.chat.id, text="*🍸Алкогольные напитки🍸*\n\nВодка «Finland»\n_100pyб._\n\nСваяк\n"
                                               "_8руб._\n\nСтарка\n_8руб._\n\nВиски «Passport Scotch»\n_50руб._\nВиски "
                                               "«Jack Daniel's»\n_150руб_\nВиски «Сhivas Regal 12 "
                                               "лет»\n_120руб._\nВиски «Monkey Shoulder»\n_250руб._\n"
                                               "Виски «Ballantine's Finest»\n_75руб._\n\nВермут «Martini "
                                               "Bianco»\n_35руб._\n\nВино «JP Chenet»\n_40руб._\n"
                                               "Вино игристое «Reguta Ribolla»\n_40руб._\nВино игристое «Lambrusco "
                                               "Lunato»\n_25руб._\nВино игристое «BOSCA»\n_25руб._ "
                                               "\n\nСоветское Шампанское\n_12руб_.", parse_mode='Markdown')
    elif message.text == "Напитки":
        bot.send_message(message.chat.id, text="*Напитки*\n\nCoca Cola(в ассортименте)\n_3.0pуб._\n\nFanta\n_3.0руб._\n"
                                               "\nSprite\n_3.0руб._\n\nBurn\n_5.0руб._\n\nВода Bonaqua "
                                               "газ./негаз.\n_2.5руб._\n\nБалтика 0 Пшеничное\n_4.0руб._\n\nБалтика 0 "
                                               "Грейпфрут\n_3.0руб_", parse_mode='Markdown')

    elif message.text == "Кальян":
        bot.send_message(message.chat.id, text="*Кальян*\n\nКальян премиум\n_31руб._\n\n❗При заказе второго кальяна "
                                               "цена - 27руб.❗", parse_mode='Markdown')

    elif message.text == "Снэки":
        bot.send_message(message.chat.id, text="*Cнэки*\n\nLays маленький/средний/большой\n_2.0/4.0/6.0руб._\n\n"
                                               "Попкорн "
                                               "70гр\n_2.0руб._\n\nПопкорн 180гр\n_3.0руб._\n\nСухарики "
                                               "Хрусteam\n_1.5руб._\n\nCabandos\n_5.0руб_\n\nКальмар\n_4.0руб_\n\n"
                                               "Жвачка\n_2 "
                                               ".0руб._\n\nSnikers/Twix/kitkat\n_2.0руб._",
                         parse_mode='Markdown')

        # При нажатии на кнопку прайс , появляется 5 кнопок с комнатами + вернуться в главное меню
    elif message.text == "❓ Расскажи про комнаты":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Голубая🎲🧩")
        btn2 = types.KeyboardButton("Желтая🍸")
        btn3 = types.KeyboardButton("Фиолетовая🍔🍟")
        btn4 = types.KeyboardButton("Серая🎤")
        btn5 = types.KeyboardButton("Коричневая🎮")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выбирай комнату и я расскажу о ней", reply_markup=markup)


    # 5 кнопок + изображение каждой комнаты
    elif message.text == "Голубая🎲🧩":
        bot.send_message(message.chat.id,
                         text="🔵 *Голубая комната* 🔵\n\n⚡️ Вмещает до 7 человек\n\n⚡️ Большой диван и кресла "
                              "мешки\n\n⚡️ Большой "
                              "телевизор на 55 дюймов с 4к\n\n⚡️ Мощная аудиосистема\n\n⚡️ Большой стол, специально "
                              "для наших "
                              "настольных игр и ваших напитков😉",
                         parse_mode="Markdown")
        img1 = "https://wampi.ru/image/RhIZ90E"
        bot.send_photo(message.chat.id, img1)
    elif message.text == "Желтая🍸":
        bot.send_message(message.chat.id,
                         text="🟡 *Жёлтая комната* 🟡\n\n САМАЯ ПРИВАТНАЯ КОМНАТА ПЛОЙКИ!\n\n3̶ ̶к̶р̶е̶с̶л̶а̶ "
                              "̶м̶е̶ш̶к̶а̶  → ❗️*Комфортный диван до 4 человек* ❗ \n\n-Лед-подстветка и напольный "
                              "светильник.\n\n-Подписка на IVI для ещё более комфортного просмотра фильмов.\n\n"
                              "-Маленький столик для ваших напитков и еды.", parse_mode="Markdown")
        img2 = "https://wampi.ru/image/RhIjjIs"
        bot.send_photo(message.chat.id, img2)
    elif message.text == "Фиолетовая🍔🍟":
        bot.send_message(message.chat.id,
                         text="🟣 *Фиолетовая комната* 🟣\n\nКомфортный диван с подушками + *кресло-мешок*\n\nЛед "
                              "подсветка для атмосферы эйфории🔥\n\nСамые новые и любимые игры наших "
                              "посетителей!\n_P.S Подпишись на наш инстаграм, там мы постоянно проводим опросы касаемо "
                              "игр и самые популярные ответы появляются на всех PS4!_\n\n "
                              "*‼️Закрывается "
                              "шторкой ‼️*", parse_mode="Markdown")
        img3 = "https://wampi.ru/image/RhIrsYn"
        bot.send_photo(message.chat.id, img3)

    elif message.text == "Серая🎤":
        bot.send_message(message.chat.id,
                         text="⚪️*Серая комната* ⚪\n\n САМАЯ ОСНАЩЕННАЯ КОМНАТА ПЛОЙКИ!\n\nДиван и кресла мешки → "
                              "❗️*ДВОЙНОЙ КОМФОРТ "
                              "* ❗ 2 дивана и кресла мешки\n\n"
                              "Большой "
                              "телевизор на 60 дюймов + мощнейшая аудиосистема\n\n❗️*Cистема домашнего кинотеатра для "
                              "объёмного звука при игре в PS/просмотре фильмов* ❗\n_P.S Теперь слушать ваши любимые "
                              "песни можно еще громче_ ", parse_mode="Markdown")
        img4 = "https://wampi.ru/image/RhIrJBq"
        img5 = "https://wampi.ru/image/RkULOHH"
        img6 = "https://wampi.ru/image/RkULakZ"
        bot.send_photo(message.chat.id,
                       img4)
        bot.send_photo(message.chat.id,
                       img5)
        bot.send_photo(message.chat.id,
                       img6)

    elif message.text == "Коричневая🎮":
        bot.send_message(message.chat.id,
                         text="🟤 *Коричневая комната* 🟤\n\nБольшой диван + кресла мешки → *ВМЕЩАЕТ ДО 10 ЧЕЛОВЕК*\n\n"
                              "✅ Большой телевизор на 55 дюймов и мощная аудиосистема\n\n✅ Большой стол, специально "
                              "для наших "
                              "настольных игр и ваших напитков😉\n\n✅ Закрывается на ключ", parse_mode="Markdown")
        img7 = "https://wampi.ru/image/RhIr0mw"
        img8 = "https://wampi.ru/image/RkULTr4"
        bot.send_photo(message.chat.id,
                       img7)
        bot.send_photo(message.chat.id,
                       img8)
    elif message.text == "Сообщить о проблеме":
        bot.send_message(message.chat.id,
                         text="*❗Внимание❗*\n\n_Не забывайте указывать ваше имя и номер для связи.Если "
                              "проблема требует незамедлительного решения, пожалуйста, позвоните по "
                              "этому номеру(номер админа)_", parse_mode="Markdown")
        probl = bot.send_message(message.chat.id, text="Распишите пожалуйста суть вашей проблемы и я передам ее "
                                                       "администратору для решения.\n*Приносим свои извинения за "
                                                       "предоставленные "
                                                       "неудобства!*", reply_markup=keyboard, parse_mode="Markdown")
        bot.register_next_step_handler(probl, get_problem)



    # Возвращает в самое начало
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("📅 Забронировать комнату")
        markup.row(btn1)
        btn2 = types.KeyboardButton("❓ Расскажи про комнаты")
        markup.row(btn2)
        btn3 = types.KeyboardButton("✅ Прайс")
        btn4 = types.KeyboardButton("🥂 Ployka Бар")
        markup.row(btn3, btn4)
        btn5 = types.KeyboardButton("Сообщить о проблеме")
        markup.row(btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    # Принимает бронь у человека 1) запрашивает имя
    elif message.text == "📅 Забронировать комнату":
        name = bot.send_message(message.from_user.id, 'Введите ваше имя для бронирования комнаты ',
                                reply_markup=keyboard)

        bot.register_next_step_handler(name, get_age)
    else:
        bot.send_message(message.chat.id, text='Упс.Такой команды я не знаю.')


bot.message_handler(content_types=['text'])


# 2) получает имя и запрашивает возраст для информирования пользователя о его возможностях на территории заведения
def get_age(message):
    global name_of_person
    age_of = bot.send_message(message.chat.id, text='Введите ваш возраст(цифрами).')
    name_of_person = message.text

    bot.register_next_step_handler(age_of, get_number_of_people)


# 3) получает возраст , выдает информацию + запрашивает количество человек для помощи в подборе комнаты
def get_number_of_people(message):
    global age
    age = int(message.text)
    if age < 18:
        bot.send_message(message.chat.id,
                         text='‼️*Уважаемые посетители плойки* ‼ \n\n _Информируем вас о том, что в связи с '
                              'законодательством '
                              'РБ на территории заведения несовершенолетним запрещается: распивать и приобретать '
                              'алкогольные напитки, курить кальян, а так же приобретать HQD у администратора.Спасибо '
                              'за понимание!_️', parse_mode="Markdown")
    elif age > 18:
        bot.send_message(message.chat.id,
                         text='✅️*Уважаемые посетители плойки* ✅\n\n_Спешим информировать вас о том, '
                              'что на территории нашего '
                              'заведения вы всегда можете заказать кальян, а так же приобрести алкогольные напитки.С '
                              'уважением, администация плойки!_', parse_mode="Markdown")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("<3")
    btn2 = types.KeyboardButton("4-5")
    btn3 = types.KeyboardButton("до 7")
    btn4 = types.KeyboardButton("до 10")
    btn5 = types.KeyboardButton("до 20")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    number_of_people = bot.send_message(message.chat.id,
                                        text='Выберите количество человек, которое планиркет посетить комнату.',
                                        reply_markup=markup)
    bot.register_next_step_handler(number_of_people, get_room)


# 4) получает количество человек , подбирает комнату исходя из количества человек комнату
@bot.message_handler(content_types=['text'])
def get_room(message):
    if message.text == '<3':
        bot.send_message(message.chat.id,
                         text='Для такого количества человек идеально подойдет:\n\n🟡*Желтая '
                              'вип-комната*🟡\n\n🟢*Общий зал*🟢', parse_mode='Markdown')
    elif message.text == '4-5':
        bot.send_message(message.chat.id,
                         text='Для вашего комфорта стоит выбрать 🟣*Фиолетовую вип-комнату'
                              '*🟣 или же 🟢*Общий зал*🟢(4 человека)', parse_mode='Markdown')
    elif message.text == 'до 7':
        bot.send_message(message.chat.id,
                         text='Лучшим вариантом для такой компании станет 🔵*Голубая вип-комната*🔵',
                         parse_mode='Markdown')
    elif message.text == 'до 10':
        bot.send_message(message.chat.id,
                         text='Для больших компаний предусмотрено две вип-комнаты:\n⚪Серая вип-комната⚪\n(подойдет для '
                              'людей , предпочитающих повышенный комфорт) имеет *два дивана + кресла '
                              'мешки*\n🟤Коричневая вип-комната🟤\nимеет один диван + кресла мешки',
                         parse_mode='Markdown')
    elif message.text == 'до 20':
        bot.send_message(message.chat.id,
                         text='Для масштабных мероприятий(корпоратив, день рождения) плойка предлагает возможность '
                              '‼*СЪЕМА ВСЕГО ОБЩЕГО ЗАЛА*‼ всего за _50 руб./час_ для максимального комфорта Вас и '
                              'Ваших гостей',
                         parse_mode='Markdown')
    # 5)Создает 7 кнопок для выбора комнаты
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Голубая🎲🧩")
    btn2 = types.KeyboardButton("Желтая🍸")
    btn3 = types.KeyboardButton("Фиолетовая🍔🍟")
    btn4 = types.KeyboardButton("Серая🎤")
    btn5 = types.KeyboardButton("Коричневая🎮")
    btn6 = types.KeyboardButton("Общий зал🎉")
    btn7 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    room = bot.send_message(message.chat.id,
                            text='Выберите комнату, которую вы хотите забронировать.', reply_markup=markup)
    bot.register_next_step_handler(room, get_telephone)


# 6)Подтверждает комнату + запрашивает номер телефона
def get_telephone(message):
    global rooms
    rooms = message.text
    if message.text == "Голубая🎲🧩":

        bot.send_message(message.chat.id,
                         text=f"Вы выбрали {message.text} вип-комнату")

    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("📅 Забронировать комнату")
        markup.row(btn1)
        btn2 = types.KeyboardButton("❓ Расскажи про комнаты")
        markup.row(btn2)
        btn3 = types.KeyboardButton("✅ Прайс")
        btn4 = types.KeyboardButton("🥂 Ployka Бар")
        markup.row(btn3, btn4)
        btn5 = types.KeyboardButton("Сообщить о проблеме")
        markup.row(btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif message.text == "Желтая🍸":
        bot.send_message(message.chat.id,
                         text=f"Вы выбрали {message.text} вип-комнату")

    elif message.text == "Фиолетовая🍔🍟":
        bot.send_message(message.chat.id,
                         text=f"Вы выбрали {message.text} вип-комнату")

    elif message.text == "Серая🎤":
        bot.send_message(message.chat.id,
                         text=f"Вы выбрали {message.text} вип-комнату")

    elif message.text == "Коричневая🎮":
        bot.send_message(message.chat.id,
                         text=f"Вы выбрали {message.text} вип-комнату")
    elif message.text == 'Общий зал🎉':
        bot.send_message(message.chat.id,
                         text=f"Вы выбрали {message.text} ")

    tel = bot.send_message(message.from_user.id, 'Введите Ваш номер телефона для завершения брони.',
                           reply_markup=keyboard)

    bot.register_next_step_handler(tel, cheak_telephone)


# 7) Завершает бронь и подверждает всю информацию
def cheak_telephone(message, keyboard=None):
    global tel_of_person
    tel_of_person = message.text
    if len(tel_of_person) != 13:
        cheak = bot.send_message(message.from_user.id,
                                 text="Проверьте правильность набранного номера.Введите номер (+375("
                                      "ХХ)ХХХХХХХ)", reply_markup=keyboard)
        bot.register_next_step_handler(cheak, change_telephone)
    else:
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)

        question = f'Ваше имя {name_of_person} и номер телефона {tel_of_person}.Бронь будеть оформлена на {rooms}.Верно ' \
                   f'ли  указана вся информация? '
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        bot.forward_message(TO_CHAT_ID, message.from_user.id, message.message_id)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes":

                bot.send_message(call.message.chat.id,
                                 text='Бронь передана , в ближайшее время с вами свяжется администатор для '
                                      'подтверждения '
                                      'брони.\nСпасибо, что выбрали именно нас!')

            elif call.data == "no":
                bot.send_message(call.message.chat.id,
                                 text='Если возникла ошибка при бронировании, следует повторить операцию '
                                      'бронирования сначала.')


def change_telephone(message):
    telephone = message.text
    bot.send_message(message.chat.id, text=f"Ваш номер телефона {telephone}")

    if message.text == "НЕТ":
        bot.send_message(message.from_user.id, text='Если возникла ошибка при бронировании, следует повторить операцию'
                                                    'бронирования сначала.')


    else:
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)

        question = f'Ваше имя {name_of_person} и номер телефона {telephone}.Бронь будеть оформлена на {rooms}.Верно ' \
                   f'ли  указана вся информация? '
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes":

                bot.send_message(call.message.chat.id,
                                 text='Бронь передана , в ближайшее время с вами свяжется администатор для подтверждения '
                                      'брони.\nСпасибо, что выбрали именно нас!')

            elif call.data == "no":
                bot.send_message(call.message.chat.id,
                                 text='Если возникла ошибка при бронировании, следует повторить операцию '
                                      'бронирования сначала.')


def get_problem(message):
    bot.forward_message(TO_CHAT_ID, message.from_user.id, message.message_id)
    bot.send_message(message.chat.id, text="Информация передана, в ближайшее время с вами свяжется администратор "
                                           "для решения проблемы.")


bot.polling(none_stop=True)
