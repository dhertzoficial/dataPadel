import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Configurações do Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "daniucs@gmail.com"  # Seu e-mail do Gmail
EMAIL_SENHA = "twyf hfdk ssxr bffw"  # Sua senha de aplicativo do Gmail
EMAIL_DESTINATARIO = "danihertz@gmail.com"

# Definir a variável to (quantidade de dias a serem somados)
to = 40  # Altere este valor conforme necessário

# Calcular a nova data
data_alvo = datetime.today() + timedelta(days=to)
dia_semana = data_alvo.strftime('%A')  # Dia da semana em inglês
data_formatada = data_alvo.strftime('%d/%m/%Y')

# Criar o assunto no formato desejado
assunto = f"Padel - {data_formatada} - {dia_semana}"

# Criar a mensagem
mensagem = f"Olá! A data alvo é {data_formatada} ({dia_semana})."

# Criar o e-mail
msg = MIMEText(mensagem)
msg["Subject"] = assunto  # Assunto curto
msg["From"] = EMAIL_REMETENTE
msg["To"] = EMAIL_DESTINATARIO

# Enviar o e-mail
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Segurança
        server.login(EMAIL_REMETENTE, EMAIL_SENHA)
        server.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, msg.as_string())
    print("E-mail enviado com sucesso!")
except Exception as e:
    print("Erro ao enviar o e-mail:", e)
