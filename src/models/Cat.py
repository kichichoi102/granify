import random

class Cat:
    def __init__(self, name=None):
        self.name = name
        self.age = random.randrange(5, 10)
        self.favoriteFood = None

        # self.prevNames is a list datastructure keeping track of all
        # previous (and current) names it has
        self.prevNames = []

        if name:
            self.prevNames.append(self.name)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getFavoriteFood(self):
        return self.favoriteFood

    def getNames(self) -> str:
        # Returns self.prevNames List if it exists from oldest to new. 
        # Even if the prevNames is empty, it will return [] so else case is not necessary
        return self.prevNames

    def getAverageNameLength(self) -> int:
        # if names were never initialized, the length of names are
        # guaranteed to be zero (obviously since it doesn't exist)
        if not self.prevNames:
            return 0
        
        # Logic to find average length for all names in self.prevNames. 
        # Add lengths and divide by number of names in self.prevNames
        res = 0
        for name in self.prevNames:
            res += len(name)

        return res/len(self.prevNames)


    def setName(self, newName:str):
        self.name = newName
        # name changed, add new name to self.prevNames
        self.prevNames.append(self.name)
    
    def setAge(self, newAge:int):
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood:str):
        self.favoriteFood = newFavoriteFood

    def speak(self, speech=None):
        print("Meow") if not speech else print(speech)
        # increment age
        self.age += 1