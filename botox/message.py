import os
from string import Template
from dataclasses import dataclass

def read_message(filename: str): 
    with open(filename, 'r') as file:
        content = file.read()
    return Template(content)