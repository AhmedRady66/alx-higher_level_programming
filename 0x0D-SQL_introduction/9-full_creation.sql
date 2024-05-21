-- script that creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table(Id INT, Name VARCHAR(256), Score INT);
INSERT INTO second_table(Id, Name, Score) VALUES(1, 'John', 10);
INSERT INTO second_table(Id, Name, Score) VALUES(2, 'Alex', 3);
INSERT INTO second_table(Id, Name, Score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(Id, Name, Score) VALUES(4, 'George', 8);