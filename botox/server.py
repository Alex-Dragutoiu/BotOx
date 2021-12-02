import smtplib
from email.mime.text import MIMEText
from abc import ABC, abstractmethod

DOMAINS = {
    'gmail': 'smtp.gmail.com:587',
    'yahoo': 'smtp.mail.yahoo.com:587'  
}

class WrongCredentialsException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
class WrongDomainException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongRecipientException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
                
class Server(ABC):

    @abstractmethod
    def send(self, receiver, msg):
        pass
               
class SMTPServer(Server):
    def __init__(self, domain, email, password):
        """ Set up the SMTP server """  
                                
        self.domain = domain
        self.email = email
        self.password = password 
        self.server = None
    
    def __enter__(self):
        self.server = smtplib.SMTP(self.domain)
            self.server.starttls()
            self.server.login(self.email, self.password) 
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def connect(self):
        try:
               
        except smtplib.SMTPAuthenticationError as e:
            print(e)
            raise WrongCredentialsException('Wrong bot credentials!')
        
    def send(self, receiver, msg):        
        try:
            self.server.sendmail(self.email, receiver['email'], msg)
        except smtplib.SMTPRecipientsRefused as e:
            print(e)
            raise WrongRecipientException('Wrong recipient credentials!')
    
    def disconnect(self):
        self.server.quit()
