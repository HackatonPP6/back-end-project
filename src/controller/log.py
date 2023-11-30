from fastapi import APIRouter
from pydantic import BaseModel
from src.service.oracle import OracleService
from src.service.jiraService import JiraServiceApi
from src.domain.logs import Logs
from src.repository.mongo.repository import MongoRepo

from src.service.logs import LogsService
from src.service.email import EmailService

class LogController:
    router = APIRouter()

    class EmailDto(BaseModel):
        assunto:str
        body:str
        destinatario:str
    @router.post("/sendemail")
    async def sendEmail(body: EmailDto):
        return EmailService.enviar_alerta(body.assunto, body.body, body.destinatario)
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
        return JiraServiceApi.getJiraInfo()
    
    @router.get("/oracleentrypoint")
    async def oracle():
        return OracleService.getOracleInfo()
    
    @router.get("/leva")
    async def leva():
        return LogsService().gerarLevaDeLogs()
    
    @router.get("/teste")
    async def hoje(log: LogDto):
        return MongoRepo().verificaRegistroDia(log)