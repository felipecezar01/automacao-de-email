import smtplib
import email.message

def enviar_email(lista_destinatarios):
    corpo_email = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        # Aqui vai todo o conteúdo do seu email, em formato HTML e CSS. Você pode pedir para o ChatGPT já criar alguns modelos para você.
    </body>
    </html>
    """

    s = smtplib.SMTP('smtp.gmail.com: 587') # Padrão
    s.starttls()
    # Use suas credenciais de login aqui
    s.login('' , '') # Aqui vai primeiro o seu email, e depois a sua senha de app. Você pode pesquisar no Youtube. Mas basta ir nas settings da sua conta do google e procurar por 'Senha de App'

    for destinatario in lista_destinatarios:
        msg = email.message.Message()
        msg['Subject'] = "" #Descrição curta
        msg['From'] = '' #Título principal
        msg['To'] = destinatario  # Destinatário individual
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)
        s.sendmail(msg['From'], [destinatario], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {destinatario}')

    s.quit()

# Lista de emails
destinatarios = ['email@email.com', 'email2@email.com']
enviar_email(destinatarios)