from datetime import datetime

class Logs():
    def __init__(self, service, status, provider):
        self.horario = datetime.now().isoformat()
        self.service = service
        self.status = status
        self.provider = provider

    def getService(self):
        return self.service
    def setService(self, service):
        self.service = service
    def getStatus(self):
        return self.status
    def setStatus(self, status):
        self.status = status
    def getProvider(self):
        return self.provider
    def setProvider(self, provider):
        self.provider = provider
    def getHorario(self):
        return self.horario
    def setHorario(self, horario):
        self.horario = horario

    def toString(self):
        print(f"Serviço: {self.service}")
        print(f"Status: {self.status}")
        print(f"Horario: {self.horario}")
        print(f"Provider: {self.provider}")

    def dictionaryTransform(self):
        return {
        "horario": self.horario,
        "status": self.status,
        "service": self.service,
        "provider": self.provider
        }
