import sys
import random
from message import read_message
from participant import read_participants
from bot import DOMAINS, EmailBot, SMTPServer


class BotOx:
    
    def __init__(self, bot, participants):
        self.participants = participants    
        self.bot = bot
        self._pair_participants()
                
    def _pair_participants(self):
        ''' Make random pairs of players '''
        
        random.shuffle(self.participants)
        for i in range(len(self.participants)):
            self.participants[i]['secret'] = self.participants[(i + 2) % len(self.participants)]['name']

    def run(self):
        self.bot.send(self.participants)  

def main():              
    email_addrs = input('Enter Bot\'s email:') 
    passwrd     = input('Enter Bot\'s password:')
    
    email_server = SMTPServer(domain=DOMAINS['gmail'], 
                              email=email_addrs,
                              password=passwrd)    
    
    app = BotOx(bot=EmailBot(email_server, read_message('../data/message.txt')), 
                participants=read_participants('../data/participants.txt'))

    app.run()
      
if __name__ == "__main__":
    main()