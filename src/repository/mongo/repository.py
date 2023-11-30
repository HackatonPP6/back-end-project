import datetime
from datetime import timedelta
from src.domain.logs import Logs
from src.infraestructure.mongo.infra import MongoDBInfra


class MongoRepo:
    def __init__(self) -> None:
        self.infra = MongoDBInfra.get_client()
        self.database = self.infra['logs']
        self.jira = self.database['jira']
        self.aws = self.database['aws']
        self.oracle = self.database['oracle']
    
    def findJiraLogs(self) -> list:
        response = self.jira.find()
        response_list = []
        for i in response:
            obj = Logs(i["service"], i["status"], i["provider"])
            obj.setHorario(i["horario"])
            response_list.append(obj)
        return response_list
    
    def findAwsLogs(self) -> list:
        response = self.aws.find()
        response_list = []
        for i in response:
            obj = Logs(i["service"], i["status"], i["provider"])
            obj.setHorario(i["horario"])
            response_list.append(obj)
        return response_list
    
    def findOracleLogs(self) -> list:
        response = self.oracle.find()
        response_list = []
        for i in response:
            obj = Logs(i["service"], i["status"], i["provider"])
            obj.setHorario(i["horario"])
            response_list.append(obj)
        return response_list
    
    def generateNewLog(self, log: dict) -> None:
        provider: str = log["provider"]
        if "Aws" in provider:
            self.aws.insert_one(log)
        elif "Oracle" in provider:
            self.oracle.insert_one(log)
        elif "Jira" in provider:
            self.jira.insert_one(log)
        else:
            raise Exception("Invalid data")
        
    def verificaRegistroDia(self, log: dict):
        provider: str = log.provider

        if "Aws" in provider:
            today = datetime.datetime.now()
            print(today)
            print(today + timedelta(days=1))
            response = self.aws.find({"data": {"$gte": today, "$lt": today + timedelta(days=1)}})
            return list(response)
        elif "Oracle" in provider:
            self.oracle.insert_one(log)
        elif "Jira" in provider:
            self.jira.insert_one(log)
        else:
            raise Exception("Invalid data")

    


