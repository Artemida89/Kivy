import subprocess, smtplib

# Тест почты
def send_mail(email, password):
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(email, password)
    message = "hashij"
    smtpserver.sendmail(email, email, message)
    smtpserver.quit()


a = 1
x = a + a

#command = "netsh wlan show profile UPC723762 key=clear"
#result = subprocess.check_output(command, shell=True)
send_mail("grishinartyomvladimirovich@gmail.ru", "hfcgenbY089")