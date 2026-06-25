from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"The booking of Train is {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"The status of the train {self.trainNo} is on time")

    def fare(self, fro, to):
        print(f"The fare of the train {self.trainNo} from {fro} to {to} is {randint(200,800)}")

t = train(12996)
t.book("Pratapgarh","Delhi")
t.getstatus()
t.fare("Pratapgarh","Delhi")