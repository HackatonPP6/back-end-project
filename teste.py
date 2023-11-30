from email.message import EmailMessage
import ssl
import smtplib
 
def enviar_alerta(subject, body, destinatario):
    email_sender = "alertadequeda@gmail.com"
    email_password = "pqlw zvng sace lejl"
 
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = destinatario
    em["Subject"] = subject
 
    em.set_content(body)
    context = ssl.create_default_context()
 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, destinatario, em.as_string())
 
 
 
subject = f"ALERTA DE QUEDA"
body = f"""
Foi verificado que está instável por agora!
"""
 
email_receiver = "viniciusdiniz122007@gmail.com"  #Email da destinatario
enviar_alerta(subject,body, email_receiver)