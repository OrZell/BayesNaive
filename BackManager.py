from Trainer import Trainer
from Loader import Loader
from Tester import Tester

class BackManager:

    def __init__(self):
        self.Loader = Loader()

    def LoadFile(self):
        self.Loader.LoadFromPath('')
        self.DataFrame = self.Loader.GetTheFile()

    def TrainingModel(self):
        self.Trainer = Trainer(self.DataFrame)
        self.Trainer.DoAllTheSession()

    def TestTheModel(self):
        self.Tester = Tester(self.DataFrame, self.Trainer)

    def LoadTrainTest(self):
        self.LoadFile()
        self.TrainingModel()
        self.TestTheModel()

    def GetTheModel(self):
        return self.Trainer.GetTheModel()
