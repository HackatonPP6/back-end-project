import pymongo
from dotenv import load_dotenv
import os
class MongoDBInfra:
    __client = None

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            load_dotenv()
            mongo_uri = os.getenv("MONGO_URI")
            if mongo_uri is None:
                raise ValueError("Erro na conexão mongoDB")
            cls.__client = pymongo.MongoClient("mongodb+srv://hacktoon:A4fW2QXjspvMMByu@cluster0.hfds5rd.mongodb.net/?retryWrites=true&w=majority")
        return cls.__client