from src.infraestructure.redis.infra import RedisInfra


class RedisRepo:
    def __init__(self):
        self.infra = RedisInfra.get_client()

    def get(self, key):
        response = self.infra.get(key)
        return response.decode("utf-8")
    def set(self, key, value):
        self.infra.set(key, value)