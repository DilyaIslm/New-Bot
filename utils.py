from clarifai.rest import ClarifaiApp
#from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from random import randint

import settings

#def get_smile(user_data):
    #if 'emoji' not in user_data:
        #smile = choice(settings.USER_EMOJI)
        #return emojize(smile, use_aliases=True)
    #return user_data['emoji'] 

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, Вы выиграли"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number} ничья"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, Вы проиграли"
    return message          

def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать собачку', KeyboardButton('Мои координаты', request_location=True), 'Заполнить анкету']
    ])

def is_dog(file_name):
    app = ClarifaiApp(api_key=settings.CLARIFAI_API_KEY)
    model = app.public_models.general_model
    responce = model.predict_by_filename(file_name, max_concepts=5)
    if responce['status']['code'] == 10000:
        for concept in responce ['outputs'][0]['data']['concepts']:
            if concept['name'] == 'dog':
               return True
    return False    


def dog_rating_inline_keyboard(image_name):
    callback_text = f'rating|{image_name}|'
    keyboard = [
        [
            InlineKeyboardButton('Нравится', callback_data=callback_text + '1'),
            InlineKeyboardButton('Не нравится', callback_data=callback_text + '-1')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


if __name__ == "__main__":
    print(is_dog('images/dog2.jpg'))
    print(is_dog('images/not_dog.jpg'))    