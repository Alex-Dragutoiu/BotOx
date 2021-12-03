import sys
import random

from botox.participant import read_users
from botox.message import read_message
from botox.bot import EmailBot
from botox.server import DOMAINS

def make_pairs(users):
    """ Makes random pairs of players """
        
    random.shuffle(users)
    for i in range(len(users)):
        users[i]['secret'] = users[(i + 2) % len(users)]['name']

def main():              
    
    """ Input the credential of your secret Santa bot """
    email_addrs = input('Enter Bot\'s email:') 
    passwrd     = input('Enter Bot\'s password:')
    
    """ Instantiate the secret Santa bot """
    secret_santa_bot = EmailBot(email=email_addrs,
                   password=passwrd,
                   domain=DOMAINS['gmail'])
    
    """ Get your custom message and the users you want to send the message to """
    message        = read_message('data/message.txt')
    participants   = read_users('data/participants.txt')

    """ make random pairs of the participants """
    make_pairs(users=participants)

    """ Subscribe all the participants to the your secre Santa bot """
    for user in participants:
        secret_santa_bot.subscribe(user)
        
    """ Send the message to the partipants with their secret """
    secret_santa_bot.send(message)    
    
if __name__ == "__main__":
    main()