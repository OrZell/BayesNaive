class Tester:

    def __init__(self, rightAnswers:list, guessAnswers:list):
        self.RightAnswers = rightAnswers
        self.GuessAnswers = guessAnswers

    def ComapereTheAnswers(self):
        self.Checks = []
        for i in range(len(self.RightAnswers)):
            if self.RightAnswers[i] == self.GuessAnswers[i]:
                self.Checks.append(True)
            else:
                self.Checks.append(False)

    def TotalRightPrecents(self):
        return self.Checks.count(True) / len(self.RightAnswers)
