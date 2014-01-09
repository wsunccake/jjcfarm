#!/bin/sh

sqlite3 test.sqlite3 <<EOF
-- CREATE table
CREATE TABLE Persons (
ID int,
Name varchar(255),
Age int
);

-- INSERT data
INSERT INTO Persons(ID, Name, Age) VALUES(1, 'John', 18);
INSERT INTO Persons VALUES(2, 'Mary', 16);

-- SELECT data
SELECT * FROM persons;
SELECT name, age FROM perSONs WHERE age >= 18;
.quit
EOF
