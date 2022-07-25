# Take Home Assignment - Kichi Choi ##

This Assignment is designed with Data Access Layer Pattern with models, migrations, and service in mind.

This README.md file will only contain the higher level details pertaining to this project. To find details about logic, please look in the files which contain comments outlining the reasoning and explanations.

## Usage (tldr) ##

### Requirements ###
1. Clone Repository to your local machine
2. Change directories to `granify`
3. Install Docker. If you don't want to install docker, then do step 6.b instead of 6.a.
4. Install Python 3.10
5. Follow the next steps:

### 6.a: Build Dockerfile ###
```
docker build -t granify .
docker run granify
```

### 6.b: Install requirements.txt ###

```
pip install -r requirements.txt
python3 -m pytest
```

For both of these options, please ensure 32 test cases pass.

### 6. Run Main and petShop ###
```
python main.py # Runs the main.py file
python petShop.py # Runs the petShop.py file
```

I could've included these scripts in the dockerfile, but I figured you guys will want to test and run them individually anyway.


## Expected Outcomes ##
```main.py```
```
Connecting to Database
Name is Currently None
Name has been changed to Garfield
Inserting Garfield into table cat
['Garfield', 'DDDD', 'Daniel']
6.0
```

```petShop.py```
```
Connecting to Database
Inserting Felix into table cat
Inserting Beeny into table dog
Inserting None into table cat
Inserting None into table cat
Inserting None into table cat
Inserting None into table dog
Inserting None into table dog
Inserting None into table dog
8
---------------------------------------
Table: cat, Timestamp: 1, Name: Felix
Table: cat, Timestamp: 3, Name: None
Table: cat, Timestamp: 4, Name: None
Table: cat, Timestamp: 5, Name: None
Table: dog, Timestamp: 2, Name: Beeny
Table: dog, Timestamp: 6, Name: None
Table: dog, Timestamp: 7, Name: None
Table: dog, Timestamp: 8, Name: None
---------------------------------------
Table: dog, Timestamp: 2, Name: Beeny
Table: dog, Timestamp: 6, Name: None
Table: dog, Timestamp: 7, Name: None
Table: dog, Timestamp: 8, Name: None
---------------------------------------
Table: dog, Timestamp: 2, Name: Beeny
---------------------------------------
Table: cat, Timestamp: 3, Name: None
---------------------------------------
```
```
Traceback (most recent call last):
  File "C:\Users\kichi\Desktop\granify\petShop.py", line 50, in <module>
    petShop.logStats()
  File "C:\Users\kichi\Desktop\granify\petShop.py", line 43, in logStats
    self.data.getLogByTimestamp(10)                     # throws exception, timestamp is out of range
  File "C:\Users\kichi\Desktop\granify\src\dataAccessLayer\Data.py", line 89, in getLogByTimestamp
    raise Exception(f"Timestamp is out of range. Acceptable range is: [0,{self.timestamp}]")
Exception: Timestamp is out of range. Acceptable range is: [0,8]
```


PLEASE NOTE:
The exception at the end is EXPECTED! If the input timestamp is out of range, it is expected to throw an exception.

## Folder Structure ##
```
granify/
    -src/
        -dataAccessLayer/
            -Data.py
        -migrations/
            -homework.sql
        -models/
            -Cat.py
            -Dog.py
        -service/
            -usually files like petShop.py would go here. I left it in the same directory as main so it is easier to test (aka don't have to change directories every time)
    -tests/
        -test_cat.py
        -test_data.py
        -test_dog.py
    Dockerfile
    main.py
    petShop.py
```

## Deeper Dive ##
As mentioned in the beginning, this follows the Data Access Layer pattern, where:
```
-`src`/
    - `dataAccessLayer`: directory contains the database interaction layer.
        - `Data.py`: part of the assignment that "accesses" the database.
    - `migrations`: contains the sql script to build the tables and example on how to insert to said tables. usually the files are named: `001_cat_table_create.sql`, `002_dog_table_create.sql`, but the assignment told me to leave it as a singular file and named `homework.sql`
    - `models`: This directory contains the "models/classes" of the Dog and Cat tables. they contain similar methods, but differ by their `speak(speech=None)` method
    - `service`: usually files like petShop.py would go here. I left it in the same directory as main so it is easier to test (aka don't have to change directories every time)
-`tests`/
    - Contains three tests: `test_cat.py`, `test_dog.py`, `test_data.py`.
    - These unit tests cover ~100% of Cat, Dog, and Data files.
```