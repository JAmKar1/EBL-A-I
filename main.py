import telebot
from telebot import types

bot = telebot.TeleBot('7918889338:AAF2f5gpw2Hp9E_yjRKbeFkNjD4d9giLmPg')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "🎉 Привет! Добро пожаловать в наш бот по пауэрлифтингу.")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEL_FZnl8N4ENngAmvarOHf0wABn5x9bXgAAjxpAAL9CblIqU6FdSNFcSQ2BA')  
    show_main_menu(message)

def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🏋🏻‍♂️Пауэрлифтинг и силовые"))
    markup.add(types.KeyboardButton("💪🏻Бодибилдинг"))
    bot.send_message(message.chat.id, "Вы в главном меню. Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🏋🏻‍♂️Пауэрлифтинг и силовые")
def handle_powerlifting_choice(message):
    show_powerlifting_options(message)

@bot.message_handler(func=lambda message: message.text == "💪🏻Бодибилдинг")
def handle_bodybuilding_choice(message):
    show_bodybuilding_options(message)

def show_powerlifting_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "🟢Начальный",
        "🟡Средний",
        "🔴Высокий",
        "📚Жимовые раскладки",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Выберите одну из тем:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["🟢Начальный", "🟡Средний", "🔴Высокий", "📚Жимовые раскладки"])
def handle_powerlifting_levels(message):
    send_excel_file(message)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def back_to_main_menu(message):
    show_main_menu(message)

def send_excel_file(message):
    excel_file_paths = {
        "🟢Начальный": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской начальный 2х2.xlsx',
        "🟡Средний": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Средний.xlsx',
        "🔴Высокий": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Высокий.xlsx',
        "📚Жимовые раскладки": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Жимовые_раскладки.xlsx'
    }

    selected_level = message.text
    file_path = excel_file_paths.get(selected_level)
    
    if file_path:
        try:
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                bot.send_message(message.chat.id, f"Вот файл для уровня: {selected_level}.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Не удалось отправить файл: {str(e)}")

def show_bodybuilding_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "👨 Мужчина",
        "👩 Женщина",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["👨 Мужчина", "👩 Женщина"])
def handle_bodybuilding_gender(message):
    show_experience_options(message, message.text)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def back_to_bodybuilding_options(message):
    show_bodybuilding_options(message)

def show_experience_options(message, gender):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Меньше года",
        "1-3 года",
        "Больше 3 лет",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, f"Вы выбрали {gender}. Выберите стаж тренировок:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Меньше года", "1-3 года", "Больше 3 лет"])
def handle_experience_selection(message):
    show_training_days_options(message)

def show_training_days_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "2x2",
        "3 дня в неделю",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Выберите количество тренировок в неделю:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["2x2", "3 дня в неделю"])
def handle_training_days_selection(message):
    if message.text == "2x2":
        handle_two_days_selection(message)
    elif message.text == "3 дня в неделю":
        handle_three_days_selection(message)


def handle_two_days_selection(message):
    excel_file_path = 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской начальный 2х2.xlsx'


    try:
        with open(excel_file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, "Вот файл для тренировки 2x2.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Не удалось отправить файл: {str(e)}")

@bot.message_handler(func=lambda message: message.text == "3 дня в неделю")
def handle_three_days_selection(message):
    excel_file_path = 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской начальный 3х дневный.xlsx'  # Путь к вашему файлу

    try:
        with open(excel_file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, "Вот файл для тренировки 3 дня в неделю.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Не удалось отправить файл: {str(e)}")

bot.polling(none_stop=True)
