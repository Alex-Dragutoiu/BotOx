
# from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from abc import ABC, abstractmethod

from botox.server import SMTPServer
from dataclasses import dataclass, field
from typing import List
from string import Template


@dataclass
class EmailBot:
    """  Sends emails to the users with the person
         They need to buy a present for 
    """

    email: str
    password: str
    domain: str
    users: List[dict] = field(default_factory=list)
    
    def send(self, message: Template):
        """ Send an email to each user """
        with SMTPServer(self.domain, self.email, self.password) as conn:    
            for u in self.users:
                msg = MIMEText(message.substitute(PARTICIPANT=u['name']), 'plain') #, SECRET=u['secret']
                msg['Subject'] = "BotOx's Secret Santa"
                msg['From'] = self.email            
            conn.sendmail(from_addr=self.email, to_addrs=u['email'], msg=msg.as_string())
    
    def subscribe(self, user: dict):
        if user in self.users:
            print(f"User with email {user['email']} has already subscribed to bot!")
            return  
        self.users.append(user)
        
    # def unsubscribe(self, user: dict):
    #     if user not in self.users:
    #         print(f"User with email {user['email']} is not an existing subscriber!")
    #         return   
    