from datetime import datetime
from random import choice
from emoji import emojize
from pymongo import MongoClient
import pymongo
import settings
import certifi

client = pymongo.MongoClient("mongodb+srv://Dilya:cAd1Qx1xb9hn5qH1@cluster0.fm2qa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl=True,ssl_cert_reqs='CERT_NONE')
#client = pymongo.MongoClient("mongodb+srv://Dilya:cAd1Qx1xb9hn5qH1@cluster0.fm2qa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.mydogbot

def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id": effective_user.id})
    if not user: 
        user = {
        "user_id": effective_user.id,
        "first_name": effective_user.first_name,
        "last_name": effective_user.last_name,
        "username": effective_user.username,
        "chat_id": chat_id,
        "emoji": emojize(choice(settings.USER_EMOJI), use_aliases=True)
    }
    db.users.insert_one(user)
    return user    

def save_anketa(db, user_id, anketa_data):
    user = db.users.find_one({"user_id": user_id})
    anketa_data['created'] = datetime.now()
    if not 'anketa' in user:
        db.users.update_one(
            {'_id': user['_id']},
            {'$set': {'anketa':[anketa_data]}}
        )
    else:
        db.users.update_one(
           {'_id': user['_id']},
           {'$push': {'anketa':[anketa_data]}} 
        ) 
     


