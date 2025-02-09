import telebot
from telebot import types
import os

bot = telebot.TeleBot('7918889338:AAF2f5gpw2Hp9E_yjRKbeFkNjD4d9giLmPg')

# Храним состояние пользователя и ID последних сообщений
user_states = {}
last_message_ids = {}

# Путь к папке с рандомными тренировками
RANDOM_TRAINING_PATH = 'D:\\TelegramBot\\BOT\\Random'

def delete_previous_messages(chat_id):
    """Удаляет предыдущие сообщения бота."""
    if chat_id in last_message_ids:
        for msg_id in last_message_ids[chat_id]:
            try:
                bot.delete_message(chat_id, msg_id)
            except Exception as e:
                print(f"Не удалось удалить сообщение: {e}")
        last_message_ids[chat_id] = []

def send_message_with_delete(chat_id, text, reply_markup=None):
    """Отправляет сообщение и удаляет предыдущие."""
    delete_previous_messages(chat_id)
    msg = bot.send_message(chat_id, text, reply_markup=reply_markup)
    if chat_id not in last_message_ids:
        last_message_ids[chat_id] = []
    last_message_ids[chat_id].append(msg.message_id)

@bot.message_handler(commands=['start'])
def start_command(message):
    send_message_with_delete(message.chat.id, "🎉 Привет! Добро пожаловать в наш бот по пауэрлифтингу.")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEL_FZnl8N4ENngAmvarOHf0wABn5x9bXgAAjxpAAL9CblIqU6FdSNFcSQ2BA')
    show_main_menu(message)

def show_main_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🏋🏻‍♂️ Пауэрлифтинг", callback_data='powerlifting')
    )
    markup.row(
        types.InlineKeyboardButton("💪🏻 Бодибилдинг", callback_data='bodybuilding')
    )
    markup.row(
        types.InlineKeyboardButton("🎲 Рандомные тренировки", callback_data='random_training')
    )
    send_message_with_delete(message.chat.id, "Вы в главном меню. Выберите опцию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'powerlifting')
def handle_powerlifting_choice(call):
    show_powerlifting_options(call.message)

def show_powerlifting_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🟢 Начальный", callback_data='Начальный')
    )
    markup.row(
        types.InlineKeyboardButton("🟡 Средний", callback_data='Средний')
    )
    markup.row(
        types.InlineKeyboardButton("🔴 Высокий", callback_data='Высокий')
    )
    markup.row(
        types.InlineKeyboardButton("📚 Жимовые раскладки", callback_data='Жимовые раскладки')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите одну из тем пауэрлифтинга:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'bodybuilding')
def handle_bodybuilding_choice(call):
    show_bodybuilding_options(call.message)

def show_bodybuilding_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🧔🏻 Мужчина", callback_data='men')
    )
    markup.row(
        types.InlineKeyboardButton("👩🏻 Женщина", callback_data='women')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите раздел бодибилдинга:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'random_training')
def handle_random_training_choice(call):
    show_random_training_levels(call.message)

def show_random_training_levels(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🟢 Легкий", callback_data='easy')
    )
    markup.row(
        types.InlineKeyboardButton("🟠 Средний", callback_data='medium')
    )
    markup.row(
        types.InlineKeyboardButton("🔴 Высокий", callback_data='hard')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите уровень сложности:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['easy', 'medium', 'hard'])
def handle_random_level_choice(call):
    user_states[call.message.chat.id] = {"training_level": call.data}
    show_training_categories(call.message)

def show_training_categories(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🏋️ Спина", callback_data='back_training')
    )
    markup.row(
        types.InlineKeyboardButton("🦵 Ноги", callback_data='legs_training')
    )
    markup.row(
        types.InlineKeyboardButton("💪 Руки", callback_data='arms_training')
    )
    markup.row(
        types.InlineKeyboardButton("🏋️♂️ Грудь", callback_data='chest_training')
    )
    markup.row(
        types.InlineKeyboardButton("🤸 Плечи", callback_data='shoulders_training')
    )
    markup.row(
        types.InlineKeyboardButton("🔥 Грудь+Спина", callback_data='chest_back_training')
    )
    markup.row(
        types.InlineKeyboardButton("💥 Руки+Плечи", callback_data='arms_shoulders_training')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите категорию тренировки:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in [
    'back_training', 'legs_training', 'arms_training', 'chest_training',
    'shoulders_training', 'chest_back_training', 'arms_shoulders_training'
])
def handle_training_category(call):
    user_state = user_states.get(call.message.chat.id, {})
    if not user_state.get("training_level"):
        send_message_with_delete(call.message.chat.id, "❌ Сначала выберите уровень сложности")
        return show_main_menu(call.message)
    
    category = call.data
    send_training_file(call.message, user_state["training_level"], category)

def send_training_file(message, level, category):
    category_mapping = {
        'back_training': "Back",
        'legs_training': "Legs",
        'arms_training': "Arms",
        'chest_training': "Chest",
        'shoulders_training': "Shoulders",
        'chest_back_training': "Chest+Back",
        'arms_shoulders_training': "Arms+Shoulders"
    }
    
    level_mapping = {
        'easy': "Easy",
        'medium': "Medium",
        'hard': "Hard"
    }
    
    try:
        file_name = f"{category_mapping[category]}.xlsx"
        file_path = os.path.join(
            RANDOM_TRAINING_PATH,
            level_mapping[level],
            file_name
        )
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                send_message_with_delete(message.chat.id, f"✅ {category_mapping[category]} - {level_mapping[level]}\nПриятной тренировки!")
        else:
            send_message_with_delete(message.chat.id, "⚠️ Файл с тренировкой не найден")
    except Exception as e:
        send_message_with_delete(message.chat.id, f"❌ Ошибка: {str(e)}")
    finally:
        user_states.pop(message.chat.id, None)

@bot.callback_query_handler(func=lambda call: call.data == 'men')
def handle_bodybuilding_men(call):
    user_states[call.message.chat.id] = {"gender": "men"}
    show_men_bodybuilding_options(call.message)

def show_men_bodybuilding_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🟢 Легкий", callback_data='men_easy')
    )
    markup.row(
        types.InlineKeyboardButton("🟠 Средний", callback_data='men_medium')
    )
    markup.row(
        types.InlineKeyboardButton("🔴 Высокий", callback_data='men_hard')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите уровень бодибилдинга для 🧔🏻мужчин:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'women')
def handle_bodybuilding_women(call):
    user_states[call.message.chat.id] = {"gender": "women"}
    show_women_bodybuilding_options(call.message)

def show_women_bodybuilding_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🟢 Легкий", callback_data='women_easy')
    )
    markup.row(
        types.InlineKeyboardButton("🟠 Средний", callback_data='women_medium')
    )
    markup.row(
        types.InlineKeyboardButton("🔴 Высокий", callback_data='women_hard')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите уровень бодибилдинга для 👩🏻женщин:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['men_easy', 'men_medium', 'men_hard', 'women_easy', 'women_medium', 'women_hard'])
def handle_bodybuilding_levels(call):
    user_state = user_states.get(call.message.chat.id, {})
    user_state["level"] = call.data
    user_states[call.message.chat.id] = user_state
    show_training_options(call.message)

def show_training_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📝 2х2", callback_data='2x2')
    )
    markup.row(
        types.InlineKeyboardButton("📝 1х3", callback_data='1x3')
    )
    markup.row(
        types.InlineKeyboardButton("🔙 Назад", callback_data='back')
    )
    send_message_with_delete(message.chat.id, "Выберите схему тренировок:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['2x2', '1x3'])
def handle_training_scheme(call):
    user_state = user_states.get(call.message.chat.id, {})
    scheme = call.data
    if user_state.get("gender") and user_state.get("level"):
        send_bodybuilding_file(call.message, user_state["gender"], user_state["level"], scheme)
    else:
        send_message_with_delete(call.message.chat.id, "Ошибка: Не удалось определить параметры")
        show_main_menu(call.message)

def send_bodybuilding_file(message, gender, level, scheme):
    file_paths = {
        "men": {
            "men_easy": {
                "2x2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Легкий 2х2.xlsx',
                "1x3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Легкий 1х3.xlsx'
            },
            "men_medium": {
                "2x2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Средний 2х2.xlsx',
                "1x3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Средний 1х3.xlsx'
            },
            "men_hard": {
                "2x2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Высокий 2х2.xlsx',
                "1x3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Мужской Высокий 1х3.xlsx'
            }
        },
        "women": {
            "women_easy": {
                "2x2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Легкий 2х2.xlsx',
                "1x3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Легкий 1х3.xlsx'
            },
            "women_medium": {
                "2x2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Средний 2х2.xlsx',
                "1x3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Средний 1х3.xlsx'
            },
            "women_hard": {
                "2x2": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Высокий 2х2.xlsx',
                "1x3": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Женский Высокий 1х3.xlsx'
            }
        }
    }

    try:
        file_path = file_paths[gender][level][scheme]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                send_message_with_delete(message.chat.id, f"✅ Файл для {gender}, уровень {level}, схема {scheme}")
        else:
            send_message_with_delete(message.chat.id, "⚠️ Файл не найден")
    except KeyError:
        send_message_with_delete(message.chat.id, "❌ Ошибка в параметрах запроса")
    except Exception as e:
        send_message_with_delete(message.chat.id, f"🚨 Ошибка: {str(e)}")
    finally:
        user_states.pop(message.chat.id, None)

@bot.callback_query_handler(func=lambda call: call.data in ['Начальный', 'Средний', 'Высокий', 'Жимовые раскладки'])
def handle_powerlifting_levels(call):
    send_excel_file(call.message, call.data)

def send_excel_file(message, level):
    excel_file_paths = {
        'Начальный': 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Начальный.xlsx',
        'Средний': 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Средний.xlsx',
        'Высокий': 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Высокий.xlsx',
        'Жимовые раскладки': 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Жимовые раскладки.docx'
    }

    file_path = excel_file_paths.get(level)
    
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)
                send_message_with_delete(message.chat.id, f"Вот файл для раздела: {level}.")
        except Exception as e:
            send_message_with_delete(message.chat.id, f"Не удалось отправить файл: {str(e)}")
    else:
        send_message_with_delete(message.chat.id, "Файл не найден.")

@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back_handler(call):
    current_state = user_states.get(call.message.chat.id, {})
    
    if current_state.get("training_level"):
        user_states.pop(call.message.chat.id, None)
        show_random_training_levels(call.message)
    elif "level" in current_state:
        if current_state.get("gender") == "men":
            show_men_bodybuilding_options(call.message)
        else:
            show_women_bodybuilding_options(call.message)
        user_states[call.message.chat.id].pop("level", None)
    elif "gender" in current_state:
        show_bodybuilding_options(call.message)
        user_states.pop(call.message.chat.id, None)
    else:
        show_main_menu(call.message)

bot.polling(none_stop=True)
