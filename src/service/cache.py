from src.domain.enum.services import Services
from src.repository.redis.repository import RedisRepo


class CacheService:
    def __init__(self):
        self.repo = RedisRepo()
    def getAllStatus(self):
        response = []
        lista_servicos = list(Services)
        for i in lista_servicos:
            dicionario = {}
            value = self.repo.get(i.value)
            dicionario[i] = value
            response.append(dicionario)
        return response