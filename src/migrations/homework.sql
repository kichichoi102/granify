-- Create Cat and Dog tables with the associated columns. See ./src/models/Cat.py or ./src/models/Dog.py to see why I used these columns.

CREATE TABLE Cat (
    CatID INT IDENTITY (1, 1) NOT NULL,
    Name VARCHAR(255),
    Age INT,
    FavoriteFood VARCHAR(255),
    CONSTRAINT [PK_CatID] PRIMARY KEY CLUSTERED ([CatID] ASC)
);

CREATE TABLE Dog (
    DogID INT IDENTITY (1, 1) NOT NULL,
    Name VARCHAR(255),
    Age INT,
    FavoriteFood VARCHAR(255),
    CONSTRAINT [PK_DogID] PRIMARY KEY CLUSTERED ([DogID] ASC)
);

-- Insert Felix cat and Beeny dog into table.
INSERT INTO Cat (Name, Age, FavoriteFood) 
VALUES ('Felix', 6, "Cheesecake");

INSERT INTO Dog (Name, Age, FavoriteFood) 
VALUES ('Beeny', 7, "Spaghetti");