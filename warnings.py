class TextNotEncrypted(Warning):
    def __init__(self, message):
        self.message = message


class EnteredEmptyString(Warning):
    def __init__(self, message):
        self.message = message
