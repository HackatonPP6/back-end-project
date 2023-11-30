import requests
import json
from src.domain.logs import Logs
from src.domain.enum.status import Status
 
class OracleService():
    def getOracleInfo():
        response = requests.get("https://ocistatus.oraclecloud.com/api/v2/components.json")
    
        document = json.loads(response.text)
        healthReports = document['regionHealthReports']
        brazilianReports = list()
        cont = 0

        tem_degradation_sp = False
        tem_degradation_vi = False
    
        for report in healthReports:
            if report['regionName'] == 'Brazil East (Sao Paulo)' or report['regionName'] == 'Brazil Southeast (Vinhedo)':
                regionName = 'Oracle ' + report['regionName']
                for service in report['serviceHealthReports']:
                    serviceName = service['serviceName']
                    status = service['serviceStatus']
                    status = Status.RESOLVED.value if status == "NormalPerformance" else Status.DEGRADATION.value
                    if not tem_degradation_sp and status == Status.DEGRADATION.value and "Sao Paulo" in report['regionName']:
                        tem_degradation_sp = True

                    if not tem_degradation_vi and status == Status.DEGRADATION.value and "Vinhedo" in report['regionName']:
                        tem_degradation_vi = True


                    brazilianReports.append(Logs(serviceName, status, regionName))
                cont+=1
            
            if cont == 2:
                break
        
        returnList = []
        for x in brazilianReports:
            returnList.append(Logs.dictionaryTransform(x))
        return [returnList, tem_degradation_sp, tem_degradation_vi]