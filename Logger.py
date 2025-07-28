import datetime

class Logger:

    def __init__(self, path):
        self.PATH = path

    @staticmethod
    def current_time():
        return datetime.datetime.now().strftime('%D %T')

    def log(self, message):
        with open(self.PATH, 'a') as file:
            file.write(f'{self.current_time()} - {message}\n')
