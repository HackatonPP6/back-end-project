from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.domain.logs import Logs
from src.domain.enum.status import Status

class AwsService:
    def get_AWS_log():
        navegador = webdriver.Chrome()
        aws_status = []

        tem_degradation_sp = False
        tem_degradation_vi = False
    
        try:
            navegador.get('https://health.aws.amazon.com/health/status')
    
            time.sleep(2)
            filtro = navegador.find_element(By.ID, 'status-history-property-filter').find_elements(By.XPATH, './/*')[10]
    
            filtro.send_keys("N. Virginia")
            filtro.send_keys(Keys.DOWN)
            filtro.send_keys(Keys.ENTER)
    
            filtro.send_keys("Sao Paulo")
            filtro.send_keys(Keys.DOWN)
            filtro.send_keys(Keys.ENTER)
            time.sleep(2)
    
            btn_aumentar = navegador.find_element(By.CLASS_NAME, "table-tray").find_element(By.TAG_NAME, "a")
    
            navegador.execute_script("arguments[0].scrollIntoView();", btn_aumentar)
            btn_aumentar.click()
    
            time.sleep(1)
            linhas = navegador.find_elements(By.TAG_NAME, 'tr')[2:]
    
            for linha in linhas:
                n_nome = linha.find_elements(By.XPATH, './/*')[3].get_attribute("innerHTML")
                n_status = Status.RESOLVED.value if linha.find_elements(By.XPATH, './/*')[15].get_attribute("aria-label").strip() == "Resolved" else Status.DEGRADATION.value
            
                if "Virginia" in n_nome:
                    n_nome = n_nome.split("(")[0] + "(N. Virginia)"
                    if not tem_degradation_vi and n_status == Status.DEGRADATION.value:
                        tem_degradation_vi = True

                    aws_status.append(Logs(n_nome, n_status, "AWS.Virginia"))
                else:
                    if not tem_degradation_sp and n_status == Status.DEGRADATION.value:
                        tem_degradation_sp = True

                    n_nome = n_nome.split("(")[0] + "(Sao Paulo)"
                    aws_status.append(Logs(n_nome, n_status, "AWS.SaoPaulo"))
        finally:
            navegador.quit()
    
        return [aws_status, tem_degradation_sp, tem_degradation_vi]