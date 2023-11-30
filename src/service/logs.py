from src.service.oracle import OracleService
from src.service.jira import JiraService
from src.domain.logs import Logs
from src.domain.enum.providers import Providers
from src.repository.mongo.repository import MongoRepo


class LogsService:


    def __init__(self):
        self.repo = MongoRepo()
        self.jira = JiraService
        self.oracle = OracleService
        self.registro_antigo = []
        self.registro_novo = []

    def getAllLogs(self) -> list:
        response = []
        list_providers = list(Providers)
        for i in list_providers:
            if i.value == "jira":
                response.append(self.repo.findJiraLogs())
            elif i.value == "aws":
                response.append(self.repo.findAwsLogs())
            elif i.value == "oracle":
                response.append(self.repo.findOracleLogs())
        return response
    
    def generateNewLog(self, log):
        obj:Logs = Logs(log.service, log.status, log.provider)
        obj_to_dict = {
            "horario": obj.getHorario(),
            "status": obj.getStatus(),
            "service": obj.getService(),
            "provider": obj.getProvider()
        }
        try:
            self.repo.generateNewLog(obj_to_dict)
            return "New log added"
        except:
            return "Invalid provider"
        
    def gerarLevaDeLogs(self):
        self.registro_novo.append(self.jira.getJiraInfo())
        self.registro_novo.append(self.oracle.getOracleInfo())
        return self.registro_novo
    
    # def verifyFirstLogOfTheDay(self):
    #     if self.registro_novo != self.registro_antigo:
    #         primeiroRegistroBanco()

    # def primeiroRegistroBanco(self, log):