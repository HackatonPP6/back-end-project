import requests
import json
from src.domain.logs import Logs
 
class OracleService():
    def getOracleInfo():
        response = requests.get("https://ocistatus.oraclecloud.com/api/v2/components.json")
    
        document = json.loads(response.text)
        healthReports = document['regionHealthReports']
        brazilianReports = list()
        cont = 0
    
        for report in healthReports:
            if report['regionName'] == 'Brazil East (Sao Paulo)' or report['regionName'] == 'Brazil Southeast (Vinhedo)':
                regionName = 'Oracle ' + report['regionName']
                for service in report['serviceHealthReports']:
                    categoryName = service['serviceCategoryName']
                    status = service['serviceStatus']
                    brazilianReports.append(Logs(categoryName, status, regionName))
                cont+=1
            
            if cont == 2:
                break
        
        return brazilianReports