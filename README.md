# Тренировачный Бот
Этот репозиторий содержит исходный код для Телеграм-бота [@Kachok_bibi_bot](http://t.me/Kachok_bibi_bot).  
Этот Telegram-бот предназначен для предоставления пользователям тренировочных программ и гайдов по различным направлениям фитнеса, таким как пауэрлифтинг, бодибилдинг и рандомные тренировки. Бот также предоставляет доступ к полезным материалам, таким как гайды по массонабору, прогрессу, травмам и спортивному питанию.

Основные функции
* ```Пауэрлифтинг```: Программы для начального, среднего и высокого уровней подготовки, а также жимовые раскладки.

* ```Бодибилдинг```: Программы для мужчин и женщин с различными уровнями сложности и схемами тренировок (2х2, 1х3).

* ```Рандомные тренировки```: Тренировки для разных групп мышц с выбором уровня сложности (легкий, средний, высокий).

* ```Гайды```: Полезные материалы по массонабору, прогрессу, травмам и спортивному питанию.

# Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
    git clone https://github.com/yourusername/telegram-fitness-bot.git
    cd telegram-fitness-bot
   ```
2. **Установка зависимостей**

   
3. **Настройте бота:**
   
    Создайте бота через BotFather и получите токен.

    Замените значение переменной bot = telebot.TeleBot('YOUR_BOT_TOKEN') на ваш токен.

4. **Запустите бота**

   ```bash
   python bot.py
   ```

# Использование
Запустите бота в Telegram, отправив команду /start.

Выберите интересующее вас направление:

```🏋🏻‍♂️ Пауэрлифтинг```

```💪🏻 Бодибилдинг```

```🎲 Рандомные тренировки```

```📚 Гайд```

Следуйте инструкциям бота для выбора уровня сложности, группы мышц или схемы тренировок.

Получите файл с тренировкой или ссылку на гайд.

Скачать по ссылке папку в ней будут все необходимые файлы и сама программа для использования бота:

(https://drive.google.com/drive/folders/10PpGMz6r1q8jBEbZU5sdJI5wrV78rZZh?usp=drive_link).

# Структура проекта

* ```main.py``` - Основной файл с логикой бота.

* ```README.md``` - Документация проекта.

# Зависимости

* ```telebot```

* ```logging```
 
* ```os```

# Логирование

Бот использует стандартный модуль logging для записи событий. Логи сохраняются в формате:

```bash
2023-10-01 12:00:00,000 - INFO - Бот успешно запущен
```

# Автор

Vozisov Artem - ISP 21-9


















