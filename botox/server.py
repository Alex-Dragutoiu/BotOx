import functools
from smtplib import SMTP
from abc import ABC, abstractmethod
from dataclasses import dataclass

DOMAINS = {
    'gmail': 'smtp.gmail.com:587',
    'yahoo': 'smtp.mail.yahoo.com:587'  
}
            
class SMTPServer:

    def __init__(self, domain: str, email: str, password: str):
        self.domain = domain
        self.email = email
        self.password = password
    
    def __enter__(self):
        self.conn = SMTP(self.domain)
        self.conn.starttls()
        self.conn.login(self.email, self.password)
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.quit()

