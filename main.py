from src.models.Cat import Cat
from src.dataAccessLayer.Data import Data

# I know the doc says instantiate the data object later
# but I believe in clustering inits in the beginning together
cat = Cat()
data = Data("Database")

if __name__ == "__main__":
    print(f"Name is Currently {cat.getName()}") # Expecting output: "Name is Currently None"

    cat.setName("Garfield")
    print(f"Name has been changed to {cat.getName()}") # Expecting output: "Name is Currently Garfield"

    data.insert("cat", cat) # Expecting output: Inserting Garfield into table cat

    cat.setName("DDDD")
    cat.setName("Daniel")
    print(cat.getNames()) # Expecting: ['Garfield', 'DDDD', 'Daniel']
    print(cat.getAverageNameLength()) # Expecting 6

