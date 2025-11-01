DROP TABLE IF EXISTS kafejnicas;
DROP TABLE IF EXISTS darbinieki;
DROP TABLE IF EXISTS pasutijumi;

CREATE TABLE IF NOT EXISTS kafejnicas(
    kafejnica_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    adrese TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS darbinieki(
    darbinieka_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    talrunis TEXT NOT NULL,
    amats TEXT NOT NULL,
    atvalinajuma TEXT NOT NULL,
    kafejnica_id INTEGER NOT NULL,
    FOREIGN KEY(kafejnica_id) REFERENCES kafejnicas(kafejnica_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS pasutijumi(
    pasutijumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    summa REAL NOT NULL,
    datums TEXT NOT NULL,
    apraksts TEXT NOT NULL,
    darbinieka_id INTEGER NOT NULL,
    FOREIGN KEY(darbinieka_id) REFERENCES darbinieki(darbinieka_id) ON DELETE CASCADE
);

INSERT INTO kafejnicas (nosaukums, adrese) VALUES
('Pie Jāņa', 'Brīvības iela 10'),
('Zelta Tase', 'Lāčplēša iela 22'),
('Kafijas Stūrītis', 'Valdemāra iela 15'),
('Siltie Rīti', 'Kr. Barona iela 5'),
('Rīta Prieks', 'Elizabetes iela 30');

INSERT INTO darbinieki (vards, uzvards, talrunis, amats, atvalinajuma, kafejnica_id) VALUES
('Jānis', 'Bērziņš', '+37120000000', 'viesmīlis', 'Jā', 1),
('Anna', 'Kalniņa', '+37121234567', 'barista', 'Nē', 1),
('Pēteris', 'Ozols', '+37122334455', 'viesmīlis', 'Nē', 2),
('Laura', 'Liepa', '+37121112222', 'vadītāja', 'Nē', 3),
('Mārtiņš', 'Vilks', '+37123456789', 'viesmīlis', 'Jā', 4);

INSERT INTO pasutijumi (summa, datums, apraksts, darbinieka_id) VALUES
(249.99, '2024-04-01', 'Produkti atvēršanai', 1),
(89.50, '2024-04-03', 'Kafijas pupiņas', 2),
(120.00, '2024-04-04', 'Krūzītes un šķīvji', 3),
(310.40, '2024-04-05', 'Virtuves piederumi', 4),
(99.99, '2024-04-06', 'Deserti', 2),
(45.00, '2024-04-07', 'Papīra maisiņi', 5);

--1. kas atvaļinājumā
SELECT vards, uzvards
from darbinieki
WHERE atvalinajuma = "Jā";

--2. pasutijumu kopskaits
SELECT COUNT(*) AS Pasutijumu_skaits
FROM Pasutijumi;

--3. katra darbinieka kopejais pasutijumu skaits
SELECT darbinieki.vards, darbinieki.uzvards, COUNT(pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
FROM  darbinieki
LEFT JOIN pasutijumi ON darbinieki.darbinieka_id = pasutijumi.darbinieka_id
GROUP BY darbinieki.darbinieka_id;

--4 katra darbinieka vislielaka pasutijuma summa
SELECT darbinieki.vards, darbinieki.uzvards, MAX(pasutijumi.summa) AS max_summa
FROM darbinieki
JOIN pasutijumi ON darbinieki.darbinieka_id=pasutijumi.darbinieka_id
GROUP BY darbinieki.darbinieka_id;

--5 katras kafejnicas pasutijumu videja summa
SELECT kafejnicas.nosaukums, ROUND(AVG(pasutijumi.summa),2) AS Videja_summa
FROM kafejnicas
JOIN darbinieki ON kafejnicas.kafejnica_id=darbinieki.kafejnica_id
JOIN pasutijumi ON darbinieki.darbinieka_id=pasutijumi.darbinieka_id
GROUP BY kafejnicas.kafejnica_id;

--6 viesmīļi
SELECT vards, uzvards, amats FROM darbinieki WHERE amats="viesmīlis";

--7. summa virs 100
SELECT * FROM pasutijumi WHERE summa>=100;

--8. kafejnica ar visvairak pasutijumiem(DESC)
SELECT kafejnicas.nosaukums, COUNT(pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
FROM kafejnicas
JOIN darbinieki ON kafejnicas.kafejnica_id=darbinieki.kafejnica_id
JOIN pasutijumi ON darbinieki.darbinieka_id=pasutijumi.darbinieka_id
GROUP BY kafejnicas.kafejnica_id
ORDER BY pasutijumu_skaits DESC;

--9. Kopējā piegāžu summa(pa kādu summu darbinieks ir piegādājis pasūtījumu)
SELECT darbinieki.vards, darbinieki.uzvards, SUM(pasutijumi.summa) AS Kopsumma
FROM darbinieki
JOIN pasutijumi ON darbinieki.darbinieka_id=pasutijumi.darbinieka_id
GROUP BY darbinieki.darbinieka_id;

--10. darbinieki, kuri veikuši vismaz 2 piegādes
SELECT darbinieki.vards, darbinieki.uzvards, COUNT(pasutijumi.pasutijumi_id) AS Pasutijumu_skaits
FROM darbinieki
JOIN pasutijumi ON darbinieki.darbinieka_id=pasutijumi.darbinieka_id
GROUP BY darbinieki.darbinieka_id
HAVING COUNT(pasutijumi.pasutijumi_id)>=2;
