# Проект Dog Bot

Dog Bot - это чат бот для Telegram, который может отправить пользователю фото собак, прислать местоположение.

## Установка
1. Клонируйте репозиторий с github
2. Создайте витруальное окружение
3. Установите зависимости 'pip install -r requirements.txt'
4. Создайте файл 'settings.py'
5. Добавьте в settings.py переменные:
'''
API_KEY = "API-ключ бота"
PROXY_URL = "Адрес прокси"
PROXY_USERNAME = "Логин на прокси"
PROXY_PASSWORD = "Пароль на прокси"
USER_EMOJI = [":sparkling_heart:", ":cookie:", ":dog:", ":cupid:", ":heart_eyes:"]
'''
6. Запустите бота командой python3 bot.py