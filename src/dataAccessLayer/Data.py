from collections import defaultdict

class Data:
    def __init__(self, database:str):
        print(f"Connecting to {database}")

        """
        Log Data Structure Design:
        - unique timestamp that increment everytime an entity is inserted
        - log: dictionary that has:

        key = tablename: str
        values = (timestamp, objectName): tuple(int, str)

        example:
        self.log = {
            "dog": [
                (1, "Beeny"),
                (2, "Dog1")
            ],
            "cat": [
                (3, "Felix"),
                (4, "cat1")
            ]

        }

        Log is grouped into tables, as expected in a database.
        - Can get ALL logs
        - Can get ALL Logs by tableName
        - Can get ALL Logs by name
        - Can get ONE Logs by timestamp

        Things to improve on:
        The reason why I added timestamp is for identification, data conflicts, and auditing.
        As you will see later down the code, I am using nested forloops for each key then each item associated with the key.
        You can probably already tell this is an O(n*m) solution for n=len(tables) and m=len(rows in table)
        To improve this (at least the timestamp search), a binary search algorithm can be implemented to reduce the time complexity to: O(log(m))
        """

        self.timestamp = 0
        self.log = defaultdict(list)

    def beginTran(self) -> None:
        print("Beginning a transaction")

    def rollback(self) -> None:
        print("Rolling back transaction")

    def insert(self, table:str, object) -> None:
        print(f"Inserting {object.getName()} into table {table}")
        self.timestamp += 1
        self.log[table].append((self.timestamp, object.getName()))

    def getTimestamp(self) -> int:
        return self.timestamp

    def getAllLogs(self) -> None:
        if self.log is None:
            print([])
            return
        
        for item in self.log:
            for values in self.log[item]:
                print(f"Table: {item}, Timestamp: {values[0]}, Name: {values[1]}")

    def getLogsByTableName(self, tableName:str) -> None:
        if self.log is None:
            print([])
            return
        
        if tableName not in self.log:
            print(f"{tableName} is not in database")
            return
        else:        
            for values in self.log[tableName]:
                print(f"Table: {tableName}, Timestamp: {values[0]}, Name: {values[1]}")

    def getLogByName(self, name:str) -> None:
        if self.log is None:
            print([])
            return

        for item in self.log:
            for values in self.log[item]:
                if values[1] == name:
                    print(f"Table: {item}, Timestamp: {values[0]}, Name: {values[1]}")
        
    def getLogByTimestamp(self, timestamp:int) -> None:
        if self.log is None:
            print([])
            return

        # Catch bad timestamp range. Only acceptable range is 0 to self.timestamp inclusive
        if timestamp > self.timestamp or timestamp < 0:
            raise Exception(f"Timestamp is out of range. Acceptable range is: [0,{self.timestamp}]")
            
        for item in self.log:
            for values in self.log[item]:
                if values[0] == timestamp:
                    print(f"Table: {item}, Timestamp: {values[0]}, Name: {values[1]}")
                    return




