import ssl
import pymongo
from urllib.parse import quote_plus as quote
#import settings

DB_NAME = "mydogbot"
DB_HOSTS =",".join([
      "cluster0-shard-00-02.fm2qa.mongodb.net:27017",
      "cluster0-shard-00-01.fm2qa.mongodb.net:27017",
      "cluster0-shard-00-00.fm2qa.mongodb.net:27017"
    ])
DB_USER = "Dilya"
DB_PASS = "cAd1Qx1xb9hn5qH1"

url = "mongodb://Dilya:cAd1Qx1xb9hn5qH1@cluster0.fm2qa.mongodb.net/?authSource=mongodb+srv://Dilya:cAd1Qx1xb9hn5qH1@cluster0.fm2qa.mongodb.net/test".format(
          user = quote(DB_USER),
          pw = quote(DB_PASS),
          hosts = DB_HOSTS,
          auth_src = DB_NAME)

conn = pymongo.MongoClient(url)

db = conn[DB_NAME]
print(db.name)

conn.close()
