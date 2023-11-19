import random, string


class KeyGenerator:
    def __init__(self) -> None:
        self.excluded_chars         = ""
        self.setup                  = False
        self.include_number         = False
        self.include_lowercase      = False
        self.include_uppercase      = False
        self.include_special_chars  = False
        self.valid_numbers          = list(string.digits)
        self.valid_lower_chars      = list(string.ascii_lowercase)
        self.valid_upper_chars      = list(string.ascii_uppercase)
        self.valid_sp_chars         = ['!','@','#','$','%','&']

    def setExcludedChars(self,chars):
        self.valid_lower_chars = [c for c in self.valid_lower_chars if c not in chars]
        self.valid_upper_chars = [c for c in self.valid_upper_chars if c not in chars]
        self.valid_numbers = [c for c in self.valid_numbers if c not in chars]
        self.valid_sp_chars = [c for c in self.valid_sp_chars if c not in chars]

    def _generatePassword(self, max_size, valid_chars, min_size=1):
        random_size = random.randint(min_size,max_size)
        random_chars_list = random.choices(valid_chars, k=random_size)
        return ''.join(random_chars_list)
    
    def _updatePassword(self, password, pass_size, min_reserved_chars,valid_chars):
        pass_word = self._generatePassword(pass_size-min_reserved_chars+1,valid_chars)
        min_reserved_chars -=1
        pass_size -= len(pass_word)
        password+=pass_word
        return (password, pass_size, min_reserved_chars)
    
    def generatePassword(self,pass_size):
        minimum_reserved_char = 0
        
        if self.include_lowercase:
            minimum_reserved_char+=1
        if self.include_uppercase:
            minimum_reserved_char+=1
        if self.include_number:
            minimum_reserved_char+=1
        if self.include_special_chars:
            minimum_reserved_char+=1

        if minimum_reserved_char == 0:
            self.include_number = True
            minimum_reserved_char = 1

        password = ""
        if self.include_lowercase:
            password, pass_size, minimum_reserved_char = self._updatePassword(password,
                                                                              pass_size,
                                                                              minimum_reserved_char,
                                                                              self.valid_lower_chars)
        if self.include_uppercase:
            password, pass_size, minimum_reserved_char = self._updatePassword(password,
                                                                              pass_size,
                                                                              minimum_reserved_char,
                                                                              self.valid_upper_chars)
        if self.include_number:
            password, pass_size, minimum_reserved_char = self._updatePassword(password,
                                                                              pass_size,
                                                                              minimum_reserved_char,
                                                                              self.valid_numbers)
        if self.include_special_chars:
            password, pass_size, minimum_reserved_char = self._updatePassword(password,
                                                                              pass_size,
                                                                              minimum_reserved_char,
                                                                              self.valid_sp_chars)
        if pass_size>0:
            if self.include_lowercase:
                password += self._generatePassword(pass_size,self.valid_lower_chars,min_size=pass_size)
            elif self.include_number:
                password += self._generatePassword(pass_size,self.valid_numbers,min_size=pass_size)
            elif self.include_uppercase:
                password += self._generatePassword(pass_size,self.valid_upper_chars,min_size=pass_size)
            else:
                password += self._generatePassword(pass_size,self.valid_lower_chars,min_size=pass_size)
        
        pass_list = list(password)
        random.shuffle(pass_list)
        return "".join(pass_list)
        
