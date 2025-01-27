import telebot
from telebot import types

bot = telebot.TeleBot('7861059169:AAF04JOLAwld7NYuE8zlioSLEuS2U7aZuyM')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "🎉 Привет! Добро пожаловать в наш бот по пауэрлифтингу.")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEL_FZnl8N4ENngAmvarOHf0wABn5x9bXgAAjxpAAL9CblIqU6FdSNFcSQ2BA')  
    show_main_menu(message)

def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🏋🏻‍♂️Пауэрлифтинг и силовые"))
    bot.send_message(message.chat.id, "Вы в главном меню. Выберите опцию:", reply_markup=markup)

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

def send_excel_file(message):
    files = {
        "🟢Начальный": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Начальный.xlsx',
        "🟡Средний": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Средний.xlsx',
        "🔴Высокий": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Высокий.xlsx',
        "📚Жимовые раскладки": 'D:\\TelegramBot\\BOT\\BBB\\Пауэр\\Жимовые раскладки.docx'
    }
    
    file_name = files.get(message.text)
    if file_name:
        try:
            with open(file_name, 'rb') as file:
                bot.send_document(message.chat.id, file)
                back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                back_markup.add(types.KeyboardButton("🔙 Назад"))
                bot.send_message(message.chat.id, "Вот файл. Нажмите 'Назад', чтобы вернуться.", reply_markup=back_markup)
        except Exception as e:
            bot.send_message(message.chat.id, f"Не удалось отправить файл: {str(e)}")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.chat.type == 'private':
        if message.text == "🏋🏻‍♂️Пауэрлифтинг и силовые":
            show_powerlifting_options(message)
        elif message.text in ["🟢Начальный", "🟡Средний", "🔴Высокий", "📚Жимовые раскладки"]:
            send_excel_file(message)
        elif message.text == "🔙 Назад":
            show_main_menu(message)

bot.polling()
