from src.models.Cat import Cat
from src.models.Dog import Dog
from src.dataAccessLayer.Data import Data

class PetShop:
    def __init__(self):
        self.data = Data("Database")

    def saveTest(self):
        cat = Cat("Felix")
        dog = Dog("Beeny") # this is my dogs name 🥰

        self.data.insert("cat", cat)
        self.data.insert("dog", dog)

    def savePetShop(self):
        cat1 = Cat()
        cat2 = Cat()
        cat3 = Cat()

        dog1 = Dog()
        dog2 = Dog()
        dog3 = Dog()

        self.data.insert("cat", cat1)
        self.data.insert("cat", cat2)
        self.data.insert("cat", cat3)
        self.data.insert("dog", dog1)
        self.data.insert("dog", dog2)
        self.data.insert("dog", dog3)

    def logStats(self):
        print(self.data.getTimestamp())                     # Expected output: 8
        print("---------------------------------------")
        self.data.getAllLogs()                              # Expected output: ALL tablenames, timestamps, names
        print("---------------------------------------")
        self.data.getLogsByTableName("dog")                 # Expected output: ALL tablename, timestamp, name where tableName == "dog"
        print("---------------------------------------")
        self.data.getLogByName("Beeny")                     # Expected output: ALL tablename, timestamp, name where name == "Beeny"
        print("---------------------------------------")
        self.data.getLogByTimestamp(3)                      # Expected output: ONE tablename, timestamp, name where timestamp == 3
        print("---------------------------------------")
        self.data.getLogByTimestamp(10)                     # throws exception, timestamp is out of range
        

petShop = PetShop()

petShop.saveTest()
petShop.savePetShop()
petShop.logStats()
