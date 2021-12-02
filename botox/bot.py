
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from abc import ABC, abstractmethod
from server import Server 

class EmailBot(Bot):
    """  Sends emails to the users with the person
    They need to buy a present for """
    
    def __init__(self, server: Server, template_msg: Template):
        self.server = server
        self.template_msg = template_msg

    def send(self, participants):
        """ Send an email with the secret to each player """
        
        self.server.connect()
        for p in participants:
            body = self.template_msg.substitute(PLAYER=p['name'], SECRET=p['secret'])
            msg = 'Subject: {}\n\n{}'.format("BotOx's Secret Santa", body)    
            self.server.send(p, msg)
        self.server.disconnect()
