from fastapi import APIRouter
from pydantic import BaseModel
from src.service.oracle import OracleService
from src.service.jira import JiraService
from src.service.aws import AwsService
from src.domain.logs import Logs
from src.repository.mongo.repository import MongoRepo
import json

from src.service.logs import LogsService

class LogController:
    router = APIRouter()

    @router.get("/allLogs")
    async def allLogs():
        return LogsService().getAllLogs()
    
    class LogDto(BaseModel):
        service:str
        status:str
        provider:str
    @router.post("/newLog")
    async def newLog(log: LogDto):
        return LogsService().generateNewLog(log)
    
    @router.get("/jiraentrypoint")
    async def jira():
        return JiraService.getJiraInfo()
    
    @router.get("/oracleentrypoint")
    async def oracle():
        return OracleService.getOracleInfo()

    @router.get("/jiraentrypointjson")
    async def jira():
        return JiraService.getJiraInfo()[0]
    
    @router.get("/oracleentrypointjson")
    async def oracle():
        return OracleService.getOracleInfo()[0]
    
    @router.get("/awsentrypointjson")
    async def aws():
        return AwsService.getAwsInfo()[0]
    
    @router.get("/leva")
    async def leva():
        return LogsService().gerarLevaDeLogs()
    
    @router.get("/teste")
    async def hoje(log: LogDto):
        return MongoRepo().verificaRegistroDia(log)