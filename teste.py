
import datetime
import redis
import pymongo
import os
redis_conn = redis.from_url("rediss://red-cljnhg1ll56s73bmv51g:Oh2kHG7Es24UsYQnWvHt0SED6wZgMq4Z@oregon-redis.render.com:6379")
mongo_conn = pymongo.MongoClient("mongodb+srv://hacktoon:A4fW2QXjspvMMByu@cluster0.hfds5rd.mongodb.net/?retryWrites=true&w=majority")
banco_mongo = mongo_conn["logs"]
collection = banco_mongo["oracle"]
for i in range(2):
    collection.insert_one({"horario": datetime.datetime.now(), "status": "active", "service": "testing", "provider": "Oracle.SaoPaulo"})
    print("inseriu 1")
