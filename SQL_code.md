<h4>7. В подключенном MySQL репозитории создать базу данных “Друзья человека”</h4>

```sql
DROP DATABASE IF EXISTS Human_friends;

CREATE DATABASE Human_friends;
```

<h4>8. Создать таблицы с иерархией из диаграммы в БД</h4>

```sql
USE Human_friends;

CREATE TABLE Pets ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);
 
CREATE TABLE Pack ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);

CREATE TABLE Dogs ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);

CREATE TABLE Cats ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);

CREATE TABLE Hamsters ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);

CREATE TABLE Horses ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL,
	type VARCHAR(150) NOT NULL,
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);

CREATE TABLE Camels ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);

CREATE TABLE Donkeys ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);
```

<h4>9. Заполнить низкоуровневые таблицы именами(животных), командами которые они выполняют и датами рождения</h4>

```sql
INSERT INTO Pets ( name, type, command, birth ) 
VALUES
('Sharik', 'Dog', 'Apport!', '2022-10-13'),
('Murzik', 'Cat', 'Ks-ks-ks!', '2021-08-11'),
('Rex', 'Dog', 'Give me your pow!', '2022-12-21'),
('Homa', 'Hamster', 'Run, baby!', '2023-09-20'),
('Stalone', 'Hamster', 'Chaw, hamser!', '2022-06-10'),
('Ryzhik', 'Cat', 'Catch a mouse!', '2020-03-15'),
('Barsik', 'Cat', 'Drink milk!', '2020-07-25'),
('Snezhok', 'Cat', 'Eat a fish!', '2023-02-24'),
('Joker', 'Dog', 'Dance!', '2021-07-14');
 
INSERT INTO Pack ( name, type, command, birth ) 
VALUES 
('Yaguar', 'Horse', 'Prrrr!', '2020-06-21'),
('Shadow', 'Horse', 'Jump!', '2021-03-06'),
('Sahara', 'Camel', 'Drink more water!', '2018-08-16'), 
('Rocky', 'Donkey', 'Push!', '2022-01-11'),
('Mahmud', 'Camel', 'Go to the desert!', '2019-02-26'), 
('Hawk', 'Horse', 'Run fast!', '2020-04-03'),
('Leni', 'Donkey', 'Eat an apple', '2021-03-21');

ALTER TABLE Pack RENAME TO Packs;

INSERT INTO Dogs (name, type, command, birth)
SELECT name, type, command, birth
FROM Pets
WHERE type = 'Dog';

INSERT INTO Cats (name, type, command, birth) 
SELECT name, type, command, birth 
FROM Pets 
WHERE type = 'Cat';
 
INSERT INTO Hamsters (name, type, command, birth) 
SELECT name, type, command, birth 
FROM Pets
WHERE type = 'Hamster';

INSERT INTO Horses (name, type, command, birth) 
SELECT name, type, command, birth 
FROM Packs 
WHERE type = 'Horse';

INSERT INTO Camels (name, type, command, birth) 
SELECT name, type, command, birth 
FROM Packs 
WHERE type = 'Camel';

INSERT INTO Donkeys (name, type, command, birth) 
SELECT name, type, command, birth 
FROM Packs
WHERE type = 'Donkey';
```

<h4>10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку. 
Объединить таблицы лошади, и ослы в одну таблицу.</h4>

```sql
DROP TABLE Camels;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM Packs 
WHERE type = 'Camel';
 
CREATE TABLE HorsesAndDonkeys ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL,
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE 
);
 
INSERT INTO HorsesAndDonkeys (name, type, command, birth) 
SELECT name, type, command, birth 
FROM Packs 
WHERE type IN ('Horse', 'Donkey');
```

<h4>11.Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года, 
но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице</h4>

```sql
CREATE TABLE YoungAnimals ( 
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL,
	command VARCHAR(150) NOT NULL, 
	birth DATE, 
	age INT 
);
 
INSERT INTO YoungAnimals (name, type, command, birth, age) 
SELECT name, type, command, birth,
TIMESTAMPDIFF(MONTH, birth, CURDATE()) AS age 
FROM Pets 
WHERE birth > CURDATE() - INTERVAL 3 YEAR AND birth <= CURDATE() - INTERVAL 1 YEAR UNION ALL 
SELECT name, type, command, birth, 
TIMESTAMPDIFF(MONTH, birth, CURDATE()) AS age 
FROM Packs 
WHERE birth > CURDATE() - INTERVAL 3 YEAR AND birth <= CURDATE() - INTERVAL 1 YEAR;
 
ALTER TABLE YoungAnimals CHANGE age age_in_months INT;
```

<h4>12. Объединить все таблицы в одну, при этом сохраняя поля, 
указывающие на прошлую принадлежность к старым таблицам.</h4>

```sql
CREATE TABLE AllAnimals ( 
	id INT AUTO_INCREMENT PRIMARY KEY, 
	name VARCHAR(150) NOT NULL, 
	type VARCHAR(150) NOT NULL, 
	command VARCHAR(150) NOT NULL, 
	birth DATE, 
	age_in_months INT, 
	origin_table VARCHAR(150) 
);

INSERT INTO AllAnimals(name, type, command, birth, age_in_months, origin_table) 
SELECT name, type, command, birth, NULL as age_in_months, 'Pets' as origin_table 
FROM Pets 
UNION All 
SELECT name, type, command, birth, NULL as age_in_month, 'Packs' as origin_table 
FROM Packs 
UNION ALL 
SELECT name, type, command, birth, age_in_months, 'YoungAnimals' as origin_table FROM YoungAnimals
UNION ALL
SELECT name, type, command, birth, NULL as age_in_months, 'Dogs' as origin_table 
FROM Dogs 
UNION All 
SELECT name, type, command, birth, NULL as age_in_month, 'Cats' as origin_table 
FROM Cats 
UNION ALL
SELECT name, type, command, birth, NULL as age_in_months, 'Hamsters' as origin_table 
FROM Hamsters
UNION ALL
SELECT name, type, command, birth, NULL as age_in_months, 'Horses' as origin_table 
FROM Horses 
UNION All 
SELECT name, type, command, birth, NULL as age_in_month, 'Donkeys' as origin_table 
FROM Donkeys;
```