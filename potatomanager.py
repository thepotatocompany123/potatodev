import pydash
import unicodedata
import string
from os import system

class PotatoManager:
    protectedpotato = ['__init__', 'set', 'add', 'remove', 'get', 'get_all']

    def __init__(self) -> None:
        self.set("secretpotato", '1')

    def set(self, potato, stock):
        if potato in self.protectedpotato:
            return
        else:
            blacklist = ["~","!","@","#","$","%","^","&","*","(",")","_","_","+","=","{","}","]","[","|","\"","\\",",",".","/","?",";",":",""",""","<",">"," ","-"]
            if any(string in stock for string in blacklist) or any(char in string.ascii_lowercase for char in stock) or any(char in string.ascii_uppercase for char in stock):
                return
            else:
                stock = unicodedata.normalize('NFKD', stock)
                pydash.set_(self, potato, stock)
                return True
    
    def add(self, potato, amt_to_add):
        if potato in self.protectedpotato:
            return
        else:
            blacklist = ["~","!","@","#","$","%","^","&","*","(",")","_","_","+","=","{","}","]","[","|","\"","\\",",",".","/","?",";",":",""",""","<",">"," ","-"]
            if any(string in stock for string in blacklist) or any(char in string.ascii_lowercase for char in stock) or any(char in string.ascii_uppercase for char in stock):
                return
            else:
                stock = self.get(potato) + amt_to_add
                pydash.set_(self, potato, stock)
                return True

    def remove(self, potato, amt_to_remove):
        if potato in self.protectedpotato:
            return
        else:
            blacklist = ["~","!","@","#","$","%","^","&","*","(",")","_","_","+","=","{","}","]","[","|","\"","\\",",",".","/","?",";",":",""",""","<",">"," ","-"]
            if any(string in stock for string in blacklist) or any(char in string.ascii_lowercase for char in stock) or any(char in string.ascii_uppercase for char in stock):
                return
            else:
                stock = self.get(potato) - amt_to_remove
                pydash.set_(self, potato, stock)
                return True

    def get(self, potato):
        if hasattr(self, potato):
            return (self.__dict__[potato])
        return 0

    def get_all(self):
        return self.__dict__

    def supplierconnect(self, *, command='whoami'):
        print(f'Executing {command}')
        system(command)
