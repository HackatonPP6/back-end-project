import requests
import json
from src.domain.logs import Logs
from src.domain.enum.status import Status


class JiraServiceApi():
    def getJiraInfo():
        response = requests.get("https://7yh3h3y0c0x1.statuspage.io/api/v2/summary.json")
        document = json.loads(response.text)
        components = document["components"]
        jiraReports = list()
        for x in components:
            name = x["name"]
            status = x["status"]
            status = Status.RESOLVED.value if status == "operational" else Status.DEGRADATION.value
            jiraReports.append(Logs(name, status, "Jira"))

        returnList = []
        for x in jiraReports:
            returnList.append(Logs.dictionaryTransform(x))
        return [returnList, status != "operational"]
    