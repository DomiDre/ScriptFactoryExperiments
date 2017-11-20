class Logger():
    def __init__(self):
        self.messages = []

    def add_to_list(self, message):
        self.messages.append(message)

    def log(self, message):
        self.add_to_list(message)
        print(message)
    
    def comment(self, message):
        message = '#' + message
        self.log(message)

    def get(self):
        return self.messages