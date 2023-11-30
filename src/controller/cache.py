from fastapi import APIRouter

# from src.repository.mongo.repository import MongoRepo
from src.service.cache import CacheService

class CacheController:
    router = APIRouter()

    @router.get("/allStatus")
    async def allStatus():
        return CacheService().getAllStatus()