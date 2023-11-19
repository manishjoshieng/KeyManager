from src.Encryptor import Encryptor
from src.JsonHandler import JSONFileEditor

class Account:
    def __init__(self,  email_id, password) -> None:
        self.username = email_id
        self.key = password
        self.name = email_id
        self.encryptor = Encryptor(password)
        self.filename = email_id
        self.josnHandler = JSONFileEditor(self.filename)
        
        try:
            self.josnHandler.add_value("name",self.name)
            self.josnHandler.add_value("email_id",self._encrypt(email_id))
            self.josnHandler.add_value("key",Encryptor.hashCode(password))
        except:
            pass
        else:
            self.josnHandler.save()


    def _encrypt(self, msg):
        return self.encryptor.encrypt(msg).decode()
    
    def _decrypt(self,msg):
        return self.encryptor.decrypt(msg.encode())
    
    def addPassword(self,website,username,password):
        passcodes = self.josnHandler.get_value("passcodes")
        if passcodes == None:
            passcodes = {}

        if passcodes.get(website) != None:
           passcodes[website].clear()
        else:
            passcodes[website] = []
        passcodes[website].append(self._encrypt(username))
        passcodes[website].append(self._encrypt(password))
        self.josnHandler.set_value("passcodes",passcodes)
        return
    
    def removePassword(self,website):
        passcodes = self.josnHandler.get_value("passcodes")
        if passcodes == None:
            return
        if passcodes.get(website) != None:
            del passcodes[website]
            self.josnHandler.update_value("passcodes",passcodes)
        return
    def getAllPasswords(self)-> dict:
            all_keys = {}
            all_codes = self.josnHandler.get_value("passcodes")
            for code in all_codes.keys():
                all_keys[code] = self.getPassword(code)
            return all_keys
        
    def getPassword(self,website):
        passcodes = self.josnHandler.get_value("passcodes")
        if passcodes is None:
            return None
        passcode = passcodes.get(website)
        if passcode != None:
            return (self._decrypt(passcode[0]),
                    self._decrypt(passcode[1]))
        
    def updatePassword(self,website,username,password):
        self.addPassword(website,username,password)
    
    def save(self):
        self.josnHandler.save()
    

