
def read_users(filename):
    participants = []    
    with open(filename, mode='r') as file:
        for line in file:
            participant = {
                "name": line.split()[0],
                "email": line.split()[1],
                "secret": "None"
            }
            participants.append(participant)
    return participants