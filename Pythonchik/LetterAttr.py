class LetterAttr:
    def __setattr__(self, key, new_string):
        value = ""
        for char in new_string:
            if char in key:
                value += char
        self.__dict__[key] = value

    def __getattr__(self, key):
        return key
