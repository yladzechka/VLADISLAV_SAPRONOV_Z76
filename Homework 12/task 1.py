'''1. Написать запрос, который будет создавать таблицу с столбцами, соответствующие рисунку 1 (Рисунок в облаке прилагается).
2. Заполнить данную таблицу (запросом).
3. Сделать запрос, который отобразит все ПК стоимостью менее 400 долларов.
4. Найти номер модели, скорость и размер жесткого диска ПК, имеющий RAM от 8 до 16 ГБ.
5. Вывести цену всех ПК, чей HD меньше 1000 ГБ.
6*. Всем ПК дороже 400 долларов поднять цену в два раза.'''

use HomeWork_12;

CREATE TABLE pc(
code INT,
model VARCHAR(50),
speed SMALLINT,
ram SMALLINT,
hd REAL,
cd VARCHAR(10),
price FLOAT
);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (0, "Samsung", 500, 18, 500, 250, 500);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (1, "Apple", 3000, 128, 1000, 1000, 2000);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (2, "ASUS", 800, 32, 1000, 1250, 700);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (3, "DELL", 1000, 64, 1500, 250, 1200);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (4, "HP", 1200, 32, 8, 750, 500);

INSERT INTO pc (code, model, speed, ram, hd, cd, price)
VALUES (5, "Horizont", 200, 4, 200, 100, 250);

SET SQL_SAFE_UPDATES = 0;

SELECT * FROM pc WHERE price < 400;

SELECT model, speed, hd FROM pc WHERE (ram >= 8 and ram <= 16);

SELECT price FROM pc WHERE hd < 1000;

UPDATE pc
SET price = price * 2 WHERE price > 400;