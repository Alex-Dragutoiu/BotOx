from string import Template
from dataclasses import dataclass

def read_message(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return Template(content)