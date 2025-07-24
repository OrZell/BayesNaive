import datetime

class Logger:

    def __init__(self, path):
        self.PATH = path

    def CurrentTime(self):
        return datetime.datetime.now().strftime('%D %T')

    def Log(self, message):
        with open(self.PATH, 'a') as file:
            file.write(f'{self.CurrentTime()} - {message}\n')
