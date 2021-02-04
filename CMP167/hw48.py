class TrainLine:

    def __init__(self,initName,initLength,initDailyRidership,initCoverageArea):
        self.name = initName
        self.length = initLength
        self.daily = initDailyRidership
        self.area = initCoverageArea

    def getName(self):
        return self.name

    def getLength(self):
        return self.length

    def riderDensity(self):
        return self.daily/self.area

def overallLength(subway):
    return 

def main():
    bronx = TrainLine("Bronx",300,2000,200)
    manhattan = TrainLine("Manhattan",100,5000,100)
    TrainLines = input("Enter a name of trainlines:")
    low = overallLength(TrainLines)
    print("The length of Subway is",low)

main()
