import redis
from dotenv import load_dotenv
import os
class RedisInfra:
    __client = None

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            load_dotenv()
            redis_uri = os.getenv("REDIS_URI")
            if redis_uri is None:
                raise ValueError("Erro na conexão redis")
            cls.__client = redis.from_url(redis_uri)
        return cls.__client