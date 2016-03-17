import smtplib

class EmailSender:
    def __init__(self):
        self.fromaddr = 'jh.folderprotection@gmail.com'

    def send(self, toaddr, folder, ip):
        msg = "\r\n".join(["From: %s" %self.fromaddr,"To: %s" %toaddr,"Subject: An attempt to access your folder ","","There was an attempt to access your folder: %s on your coumputer with the ip: %s" %folder %ip])
        username = self.fromaddr
        password = '5t6y7u8i'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(self.fromaddr, toaddr, msg)
        server.quit()
