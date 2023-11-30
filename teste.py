# from email.message import EmailMessage
# import ssl
# import smtplib
 
# def enviar_alerta(subject, body, destinatario):
#     email_sender = "alertadequeda@gmail.com"
#     email_password = "pqlw zvng sace lejl"
 
#     em = EmailMessage()
#     em["From"] = email_sender
#     em["To"] = destinatario
#     em["Subject"] = subject
 
#     em.set_content(body)
#     context = ssl.create_default_context()
 
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, destinatario, em.as_string())
 
 
 
# subject = f"ALERTA DE QUEDA"
# body = f"""
# Foi verificado que está instável por agora!
# """
 
# email_receiver = "viniciusdiniz122007@gmail.com"  #Email da destinatario
# enviar_alerta(subject,body, email_receiver)


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
tem_degradation = False

try:
    driver.get('https://jira-software.status.atlassian.com/')

    tabela = driver.find_element(By.CLASS_NAME, 'one-column')
    categorias = tabela.find_elements(By.XPATH, '*')
    brazilianReports = list()

    for categoria in categorias:
        categoria = categoria.find_elements(By.XPATH, '*')[0].find_elements(By.XPATH, '*')
        nome = categoria[0].get_attribute("innerHTML").strip()
        if "&amp;" in nome:
            nome_split = nome.split("&amp;")
            nome = nome_split[0] + "&" + nome_split[1]
        status = categoria[-2].get_attribute("innerHTML").strip()

        brazilianReports.append(nome)

finally:
    driver.quit()