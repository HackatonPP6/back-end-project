from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from src.domain.enum.status import Status
from src.domain.logs import Logs
# class JiraService():
    # def getJiraInfo():

        # options = webdriver.ChromeOptions()
        # options.enable_downloads = True
        # driver = webdriver.Remote(command_executor="https://backend-hacktoon.onrender.com", options=options)
        # tem_degradation = False
    
        # try:
        #     driver.get('https://jira-software.status.atlassian.com/')
    
        #     tabela = driver.find_element(By.CLASS_NAME, 'one-column')
        #     categorias = tabela.find_elements(By.XPATH, '*')
        #     brazilianReports = list()
    
        #     for categoria in categorias:
        #         categoria = categoria.find_elements(By.XPATH, '*')[0].find_elements(By.XPATH, '*')
        #         nome = categoria[0].get_attribute("innerHTML").strip()
        #         if "&amp;" in nome:
        #             nome_split = nome.split("&amp;")
        #             nome = nome_split[0] + "&" + nome_split[1]
        #         status = categoria[-2].get_attribute("innerHTML").strip()
        #         status = Status.RESOLVED.value if status == "Operational" else Status.DEGRADATION.value
        #         if not tem_degradation and status == Status.DEGRADATION.value:
        #             tem_degradation = True

        #         brazilianReports.append(Logs(nome, status, 'Jira'))
    
        # finally:
        #     driver.quit()
    
        # returnList = []
        # for x in brazilianReports:
        #     returnList.append(Logs.dictionaryTransform(x))
        # return [returnList, tem_degradation]