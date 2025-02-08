import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot('7918889338:AAF2f5gpw2Hp9E_yjRKbeFkNjD4d9giLmPg')

# Храним состояние пользователя
user_states = {}

# Путь к папке с рандомными тренировками
RANDOM_TRAINING_PATH = 'D:\\TelegramBot\\BOT\\Random'

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "🎉 Привет! Добро пожаловать в наш бот по пауэрлифтингу.")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEL_FZnl8N4ENngAmvarOHf0wABn5x9bXgAAjxpAAL9CblIqU6FdSNFcSQ2BA')
    show_main_menu(message)

def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🏋🏻‍♂️Пауэрлифтинг и силовые", "💪🏻Бодибилдинг", "🎲 Рандомные тренировки")
    bot.send_message(message.chat.id, "Вы в главном меню. Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🏋🏻‍♂️Пауэрлифтинг и силовые")
def handle_powerlifting_choice(message):
    show_powerlifting_options(message)

@bot.message_handler(func=lambda message: message.text == "💪🏻Бодибилдинг")
def handle_bodybuilding_choice(message):
    show_bodybuilding_options(message)

@bot.message_handler(func=lambda message: message.text == "🎲 Рандомные тренировки")
def handle_random_training_choice(message):
    show_random_training_levels(message)

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
    bot.send_message(message.chat.id, "Выберите одну из тем пауэрлифтинга:", reply_markup=markup)

def show_bodybuilding_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🧔🏻Мужчина", "👩🏻Женщина", "🔙 Назад")
    bot.send_message(message.chat.id, "Выберите раздел бодибилдинга:", reply_markup=markup)

def show_random_training_levels(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["🟢Легкий", "🟠Средний", "🔴Высокий", "🔙 Назад"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["🟢Легкий", "🟠Средний", "🔴Высокий"])
def handle_random_level_choice(message):
    user_states[message.chat.id] = {"training_level": message.text}
    show_training_categories(message)

def show_training_categories(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    categories = [
        "🏋️Спина", "🦵Ноги", "💪Руки",
        "🏋️♂️Грудь", "🤸Плечи", 
        "🔥Грудь+Спина", "💥Руки+Плечи",
        "🔙 Назад"
    ]
    markup.add(*categories)
    bot.send_message(message.chat.id, "Выберите категорию тренировки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [
    "🏋️Спина", "🦵Ноги", "💪Руки",
    "🏋️♂️Грудь", "🤸Плечи", 
    "🔥Грудь+Спина", "💥Руки+Плечи"
])
def handle_training_category(message):
    user_state = user_states.get(message.chat.id, {})
    if not user_state.get("training_level"):
        bot.send_message(message.chat.id, "❌ Сначала выберите уровень сложности")
        return show_main_menu(message)
    
    category = message.text
    send_training_file(message, user_state["training_level"], category)

def send_training_file(message, level, category):
    # Маппинг русских названий к английским путям
    category_mapping = {
        "🏋️Спина": "Back",
        "🦵Ноги": "Legs",
        "💪Руки": "Arms",
        "🏋️♂️Грудь": "Chest",
        "🤸Плечи": "Shoulders",
        "🔥Грудь+Спина": "Chest+Back",
        "💥Руки+Плечи": "Arms+Shoulders"
    }
    
    level_mapping = {
        "🟢Легкий": "Easy",
        "🟠Средний": "Medium",
        "🔴Высокий": "Hard"
    }
    
    try:
        # Формируем путь к файлу
        file_name = f"{category_mapping[category]}.docx"
        file_path = os.path.join(
            RANDOM_TRAINING_PATH,
            level_mapping[level],
            file_name
        )
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                bot.send_message(message.chat.id, f"✅ {category} - {level}\nПриятной тренировки!")
        else:
            bot.send_message(message.chat.id, "⚠️ Файл с тренировкой не найден")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {str(e)}")
    finally:
        user_states.pop(message.chat.id, None)

@bot.message_handler(func=lambda message: message.text == "🧔🏻Мужчина")
def handle_bodybuilding_men(message):
    user_states[message.chat.id] = {"gender": "🧔🏻Мужчина"}  
    show_men_bodybuilding_options(message)

@bot.message_handler(func=lambda message: message.text == "👩🏻Женщина")
def handle_bodybuilding_women(message):
    user_states[message.chat.id] = {"gender": "👩🏻Женщина"}  
    show_women_bodybuilding_options(message)

def show_men_bodybuilding_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "🟢Легкий",
        "🟠Средний",
        "🔴Высокий.",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Выберите уровень бодибилдинга для 🧔🏻мужчин:", reply_markup=markup)

def show_women_bodybuilding_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "🟢Легкий",
        "🟠Средний",
        "🔴Высокий.",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Выберите уровень бодибилдинга для 👩🏻женщин:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["🟢Легкий", "🟠Средний", "🔴Высокий."])
def handle_bodybuilding_levels(message):
    user_state = user_states.get(message.chat.id, {})
    user_state["level"] = message.text
    user_states[message.chat.id] = user_state
    show_training_options(message)

def show_training_options(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "📝2х2",
        "📝1х3",
        "🔙 Назад"
    ]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Выберите схему тренировок:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["📝2х2", "📝1х3"])
def handle_training_scheme(message):
    user_state = user_states.get(message.chat.id, {})
    scheme = message.text
    if user_state.get("gender") and user_state.get("level"):
        send_bodybuilding_file(message, user_state["gender"], user_state["level"], scheme)
    else:
        bot.send_message(message.chat.id, "Ошибка: Не удалось определить параметры")
        show_main_menu(message)

def send_bodybuilding_file(message, gender, level, scheme):
    file_paths = {
        "🧔🏻Мужчина": {
            "🟢Легкий": {
                "📝2х2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Легкий 2х2.xlsx',
                "📝1х3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Легкий 1х3.xlsx'
            },
            "🟠Средний": {
                "📝2х2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Средний 2х2.xlsx',
                "📝1х3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Средний 1х3.xlsx'
            },
            "🔴Высокий.": {
                "📝2х2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Высокий 2х2.xlsx',
                "📝1х3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Высокий 1х3.xlsx'
            }
        },
        "👩🏻Женщина": {
            "🟢Легкий": {
                "📝2х2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Легкий 2х2.xlsx',
                "📝1х3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Легкий 1х3.xlsx'
            },
            "🟠Средний": {
                "📝2х2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Средний 2х2.xlsx',
                "📝1х3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Средний 1х3.xlsx'
            },
            "🔴Высокий.": {
                "📝2х2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Высокий 2х2.xlsx',
                "📝1х3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Высокий 1х3.xlsx'
            }
        }
    }

    try:
        file_path = file_paths[gender][level][scheme]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                bot.send_message(message.chat.id, f"✅ Файл для {gender.lower()}, уровень {level}, схема {scheme}")
        else:
            bot.send_message(message.chat.id, "⚠️ Файл не найден")
    except KeyError:
        bot.send_message(message.chat.id, "❌ Ошибка в параметрах запроса")
    except Exception as e:
        bot.send_message(message.chat.id, f"🚨 Ошибка: {str(e)}")
    finally:
        user_states.pop(message.chat.id, None)

@bot.message_handler(func=lambda message: message.text in ["🟢Начальный", "🟡Средний", "🔴Высокий", "📚Жимовые раскладки"])
def handle_powerlifting_levels(message):
    send_excel_file(message)

def send_excel_file(message):
    excel_file_paths = {
        "🟢Начальный": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Начальный.xlsx',
        "🟡Средний": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Средний.xlsx',
        "🔴Высокий": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Высокий.xlsx',
        "📚Жимовые раскладки": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Жимовые раскладки.docx'
    }

    selected_level = message.text
    file_path = excel_file_paths.get(selected_level)
    
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                bot.send_message(message.chat.id, f"Вот файл для раздела: {selected_level}.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Не удалось отправить файл: {str(e)}")
    else:
        bot.send_message(message.chat.id, "Файл не найден.")

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def back_handler(message):
    current_state = user_states.get(message.chat.id, {})
    
    if current_state.get("training_level"):
        user_states.pop(message.chat.id, None)
        show_random_training_levels(message)
    elif "level" in current_state:
        if current_state.get("gender") == "🧔🏻Мужчина":
            show_men_bodybuilding_options(message)
        else:
            show_women_bodybuilding_options(message)
        user_states[message.chat.id].pop("level", None)
    elif "gender" in current_state:
        show_bodybuilding_options(message)
        user_states.pop(message.chat.id, None)
    else:
        show_main_menu(message)

bot.polling(none_stop=True)
