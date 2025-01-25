# Ведущий Мафии
Этот репозиторий содержит исходный код для Телеграм-бота [@Mafia_Line_bot](https://t.me/Mafia_Line_bot).  
Ведущий Мафии может проводить коллективные игры в мафию в группах.

# Использование
Добавьте [@Mafia_Line_bot](https://t.me/Mafia_Line_bot) в вашу группу, предоставьте ему права на удаление сообщений и используйте команды перечисленные ниже для создания и начала игры.

# Доступные команды
* ```/create``` - создать заявку для игры в мафию  
* ```/cancel``` - удалить заявку для игры в мафию  
* ```/start``` - начать игру в существующей заявке  
* ```/skip``` - создать голосование за пропуск дневного обсуждения  
* ```/end``` - создать голосование за окончание игры в мафию   
* ```/stats``` - вывести статистику  
* ```/rating``` - вывести рейтинг  
* ```/help``` - вывести текст помощи

# Правила мафии
В этой версии Ведущего Мафии четыре роли:  
* __Мирный житель__ - игрок, который не обладает особыми способностями;  
* __Мафия__ - игрок, который может убить одного мирного жителя каждую ночь;  
* __Дон мафии__ - мафиози, который каждую ночь может узнать об одном игроке, является он шерифом или нет;  
* __Шериф__ - мирный житель, который может узнать команду одного игрока каждую ночь.

Ведущий Мафии использует Callback кнопки для предоставления гладкой игры, вам не нужно переключать чат или отправлять что-либо для того, чтобы сделать ход. 

Для ходов мафии используется стрельба. В первую очередь, в начале игры, дон отдаёт приказ другим членам своей команды о порядке, в котором мафия должна стрелять в игроков. Каждую ночь есть фаза стрельбы, когда все члены мафии должны нажать на Inline кнопку в одно и то же время в тот момент, когда сообщение бота содержит в себе имя игрока, которого они должны убить. Если им это удаётся, этот игрок умрёт следующим утром. Сам приказ не влияет на успех выстрела мафии, так что вы можете использовать это для создания своей тактики.  

Настоятельно рекомендуется использовать функцию, позволяющую Ведущему Мафии удалять любое сообщение, отправленное не умирающим игроком во время его последних слов или не во время общего обсуждения. Чтобы включить её, сделайте его администратором с правом на удаление сообщений.

# Рейтинг
Каждая игра влияет на статистику игроков, из которой складывается рейтинг чата. По умолчанию каждый игрок победившей команды в мафии получает 1 очко и каждый игрок проигравшей команды в мафии теряет 1 очко.
























