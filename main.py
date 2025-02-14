import telebot
from telebot import types
import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot('7918889338:AAF2f5gpw2Hp9E_yjRKbeFkNjD4d9giLmPg')  


user_states = {}
last_message_ids = {}

RANDOM_TRAINING_PATH = 'D:\\TelegramBot\\BOT\\Random'


MASSONABORNIY_GUIDE_URL = "https://telegra.ph/YOUR_MASSONABOR_GUIDE"  
PROGRESS_GUIDE_URL = "https://telegra.ph/YOUR_PROGRESS_GUIDE"  
INJURY_GUIDE_URL = "https://telegra.ph/YOUR_INJURY_GUIDE"  
SPORTPIT_GUIDE_URL = "https://telegra.ph/YOUR_SPORTPIT_GUIDE"  
INSTRUCTION_URL = "https://telegra.ph/YOUR_INSTRUCTION_URL"  


def delete_previous_messages(chat_id):
    if chat_id in last_message_ids:
        for msg_id in last_message_ids[chat_id]:
            try:
                bot.delete_message(chat_id, msg_id)
            except Exception as e:
                logging.error(f"Failed to delete message {msg_id} in chat {chat_id}: {e}")
        last_message_ids[chat_id] = []


def send_message_with_delete(chat_id, text, reply_markup=None):
    delete_previous_messages(chat_id)
    try:
        msg = bot.send_message(chat_id, text, reply_markup=reply_markup)
        if chat_id not in last_message_ids:
            last_message_ids[chat_id] = []
        last_message_ids[chat_id].append(msg.message_id)
    except Exception as e:
        logging.error(f"Failed to send message to chat {chat_id}: {e}")


@bot.message_handler(commands=['start'])
def start_command(message):
    show_main_menu(message)


def show_main_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)  
    powerlifting_button = types.InlineKeyboardButton("🏋🏻‍♂️ Пауэрлифтинг", callback_data='powerlifting')
    bodybuilding_button = types.InlineKeyboardButton("💪🏻 Бодибилдинг", callback_data='bodybuilding')
    random_training_button = types.InlineKeyboardButton("🎲 Рандомные тренировки", callback_data='random_training')
    guide_button = types.InlineKeyboardButton("📚 Гайд", callback_data='guide')

    markup.add(powerlifting_button, bodybuilding_button, random_training_button, guide_button) 
    send_message_with_delete(message.chat.id, "⚡️ Выберите категорию тренировок:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'powerlifting')
def handle_powerlifting_choice(call):
    show_powerlifting_options(call.message)


def show_powerlifting_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🟢 Начальный", callback_data='Начальный'))
    markup.row(types.InlineKeyboardButton("🟡 Средний", callback_data='Средний'))
    markup.row(types.InlineKeyboardButton("🔴 Высокий", callback_data='Высокий'))
    markup.row(types.InlineKeyboardButton("📚 Жимовые раскладки", callback_data='Жимовые раскладки'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(message.chat.id,
                              "🏋🏻‍♂️Пауэрлифтинг: \nℹ️ Программы начального и среднего уровней подходят и мужчинам, и женщинам.  Инструкции внутри файла!",
                              reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'bodybuilding')
def handle_bodybuilding_choice(call):
    show_bodybuilding_options(call.message)


def show_bodybuilding_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("ℹ️ Инструкция", url=INSTRUCTION_URL))
    markup.row(types.InlineKeyboardButton("🧔🏻 Мужчина", callback_data='men'))
    markup.row(types.InlineKeyboardButton("👩🏻 Женщина", callback_data='women'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(message.chat.id, "💪🏻Бодибилдинг: Выберите пол:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'random_training')
def handle_random_training_choice(call):
    show_random_training_levels(call.message)


def show_random_training_levels(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🟢 Легкий", callback_data='easy'))
    markup.row(types.InlineKeyboardButton("🟠 Средний", callback_data='medium'))
    markup.row(types.InlineKeyboardButton("🔴 Высокий", callback_data='hard'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(message.chat.id, "🎲 Рандомная тренировка: Выберите сложность:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['easy', 'medium', 'hard'])
def handle_random_level_choice(call):
    user_states[call.message.chat.id] = {"training_level": call.data}
    show_training_categories(call.message)


def show_training_categories(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🏋️ Спина", callback_data='back_training'))
    markup.row(types.InlineKeyboardButton("🦵 Ноги", callback_data='legs_training'))
    markup.row(types.InlineKeyboardButton("💪 Руки", callback_data='arms_training'))
    markup.row(types.InlineKeyboardButton("🏋️♂️ Грудь", callback_data='chest_training'))
    markup.row(types.InlineKeyboardButton("🤸 Плечи", callback_data='shoulders_training'))
    markup.row(types.InlineKeyboardButton("🔥 Грудь+Спина", callback_data='chest_back_training'))
    markup.row(types.InlineKeyboardButton("💥 Руки+Плечи", callback_data='arms_shoulders_training'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(message.chat.id, "🎲 Рандомная тренировка: Выберите группу мышц:", reply_markup=markup)


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
        file_path = os.path.join(RANDOM_TRAINING_PATH, level_mapping[level], file_name)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(message.chat.id, file)

              
                markup = types.InlineKeyboardMarkup()
                markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))

                send_message_with_delete(message.chat.id,
                                          f"✅ {category_mapping[category]} - {level_mapping[level]}\nПриятной тренировки!",
                                          reply_markup=markup)
        else:
            send_message_with_delete(message.chat.id, "⚠️ Файл с тренировкой не найден")
    except Exception as e:
        send_message_with_delete(message.chat.id, f"❌ Ошибка: {str(e)}")
        logging.exception("Error sending training file:")
    finally:
        user_states.pop(message.chat.id, None)


@bot.callback_query_handler(func=lambda call: call.data == 'men')
def handle_bodybuilding_men(call):
    user_states[call.message.chat.id] = {"gender": "men"}
    show_men_bodybuilding_options(call.message)


def show_men_bodybuilding_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🟢 Легкий", callback_data='men_easy'))
    markup.row(types.InlineKeyboardButton("🟠 Средний", callback_data='men_medium'))
    markup.row(types.InlineKeyboardButton("🔴 Высокий", callback_data='men_hard'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(message.chat.id, "Выберите уровень для 🧔🏻мужчин:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'women')
def handle_bodybuilding_women(call):
    user_states[call.message.chat.id] = {"gender": "women"}
    show_women_bodybuilding_options(call.message)


def show_women_bodybuilding_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🟢 Легкий", callback_data='women_easy'))
    markup.row(types.InlineKeyboardButton("🟠 Средний", callback_data='women_medium'))
    markup.row(types.InlineKeyboardButton("🔴 Высокий", callback_data='women_hard'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(message.chat.id, "Выберите уровень для 👩🏻женщин:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['men_easy', 'men_medium', 'men_hard', 'women_easy',
                                                             'women_medium', 'women_hard'])
def handle_bodybuilding_levels(call):
    user_state = user_states.get(call.message.chat.id, {})
    user_state["level"] = call.data
    user_states[call.message.chat.id] = user_state
    show_training_options(call.message)


def show_training_options(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("📝 2х2", callback_data='2x2'))
    markup.row(types.InlineKeyboardButton("📝 1х3", callback_data='1x3'))
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
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

                markup = types.InlineKeyboardMarkup()
                markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))

                send_message_with_delete(message.chat.id, f"✅ Файл для {gender}, уровень {level}, схема {scheme}",
                                          reply_markup=markup)
        else:
            send_message_with_delete(message.chat.id, "⚠️ Файл не найден")
    except KeyError:
        send_message_with_delete(message.chat.id, "❌ Ошибка в параметрах запроса")
    except Exception as e:
        send_message_with_delete(message.chat.id, f"🚨 Ошибка: {str(e)}")
        logging.exception("Error sending bodybuilding file:")
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

             
                markup = types.InlineKeyboardMarkup()
                markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))

                send_message_with_delete(message.chat.id, f"Вот файл для раздела: {level}.", reply_markup=markup)
        except Exception as e:
            send_message_with_delete(message.chat.id, f"Не удалось отправить файл: {str(e)}")
            logging.exception("Error sending Excel file:")
    else:
        send_message_with_delete(message.chat.id, "Файл не найден.")


@bot.callback_query_handler(func=lambda call: call.data == 'guide')
def handle_guide_choice(call):
    show_guide_options(call.message)


def show_guide_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2) 
    massonabor_button = types.InlineKeyboardButton("💪🏻 Массонабор", callback_data='massonabor_guide')
    progress_button = types.InlineKeyboardButton("📈 Прогресс", callback_data='progress_guide')
    injury_button = types.InlineKeyboardButton("🤕 Травмы", callback_data='injury_guide')
    sportpit_button = types.InlineKeyboardButton("💊 Спортпит", callback_data='sportpit_guide')
    back_button = types.InlineKeyboardButton("🔙 Назад", callback_data='back')

    markup.add(massonabor_button, progress_button, injury_button, sportpit_button, back_button) 

    send_message_with_delete(message.chat.id, "📚 Выберите гайд:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'massonabor_guide')
def handle_massonabor_guide(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(call.message.chat.id, f"📖 Держи гайд:\n{MASSONABORNIY_GUIDE_URL}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'progress_guide')
def handle_progress_guide(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(call.message.chat.id, f"📖 Держи гайд:\n{PROGRESS_GUIDE_URL}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'injury_guide')
def handle_injury_guide(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(call.message.chat.id, f"📖 Держи гайд:\n{INJURY_GUIDE_URL}", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sportpit_guide')
def handle_sportpit_guide(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(call.message.chat.id, f"📖 Держи гайд:\n{SPORTPIT_GUIDE_URL}", reply_markup=markup)


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


@bot.callback_query_handler(func=lambda call: call.data == 'massonabor_guide')
def handle_massonabor_guide(call):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("🔙 Назад", callback_data='back'))
    send_message_with_delete(call.message.chat.id, f"📖 Держи гайд:\n{MASSONABORNIY_GUIDE_URL}", reply_markup=markup)


bot.polling(none_stop=True)

