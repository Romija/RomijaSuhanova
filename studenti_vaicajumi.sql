DROP TABLE IF EXISTS atzimes;
DROP TABLE IF EXISTS studentu_kursi;
DROP TABLE IF EXISTS kursi;
DROP TABLE IF EXISTS studenti;

--studenti - glabā studentu pamatinformāciju
CREATE TABLE IF NOT EXISTS studenti(
    studenti_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    epasts NOT NULL UNIQUE CHECK(epasts LIKE '%@%')
);

CREATE TABLE IF NOT EXISTS kursi(
    kursa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL UNIQUE,
    apraksts TEXT DEFAULT 'Nav apraksta'
);

CREATE TABLE IF NOT EXISTS studentu_kursi(
    studentu_kursi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studenta_id INTEGER NOT NULL, --norāde uz tabulu studenti
    kursa_id INTEGER NOT NULL, --norāde uz tabulu kursi
    --viens students nevar būt divreiz pieraksstīts tajā pašā kursā
    UNIQUE(studenta_id, kursa_id),

    FOREIGN KEY(studenta_id) REFERENCES studenti(studenti_id) ON DELETE CASCADE,
    --ja izdzēs studentu vai kursu, tad attiecīgos pierakstus dzēš automātiski
    FOREIGN KEY(kursa_id) REFERENCES kursi(kursi_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS atzimes(
    atzimes_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studenta_id INTEGER NOT NULL,
    kursa_id INTEGER NOT NULL,
    --atzīme no 1-10
    atzime INTEGER NOT NULL CHECK(atzime BETWEEN 1 AND 10),
    FOREIGN KEY(studenta_id) REFERENCES studenti(studenti_id) ON DELETE CASCADE,
    FOREIGN KEY(kursa_id) REFERENCES kursi(kursi_id) ON DELETE CASCADE
    --kombinācija studenta_id un kursa_id nevar atkārtoties
    UNIQUE(studenta_id, kursa_id)
);

--studentu pievienošana
INSERT INTO studenti(vards,uzvards,epasts) VALUES
    ('Reinis','Kurpnieks','reinis.kurpnieks@gmail.com'),
    ('Elza','Rava','elza.rava@gmail.com'),
    ('Labs','Butibs','labs.butibs@gmail.com'),
    ('Alise','Salde','alise.salde@gmail.com');

--kursu pievienošana
INSERT INTO kursi(nosaukums,apraksts) VALUES
    ('Matemātika','Algebra un ģeometrija'),
    ('Angļu valoda','C1 līmenī'),
    ('Bioloģija','Augu attīstība'),
    ('Biofizika','Bioloģija saistībā ar fiziku');

--studentu pierakstīšana kursos
INSERT OR IGNORE INTO studentu_kursi(studenta_id, kursa_id) VALUES
    (1,2),(1,4),(1,1), -- Reinis
    (2,1), --Elza
    (3,4),(3,3), -- Labs
    (4,2); -- Alise

INSERT OR IGNORE INTO atzimes(studenta_id,kursa_id,atzime) VALUES
    (1,2,9),
    (1,4,3),
    (1,1,6),
    (2,1,2),
    (3,4,10),
    (3,3,8),
    (4,2,7);

--visus studentus parādīt dilstošā secībā pēc uzvārda
SELECT * FROM studenti ORDER BY uzvards DESC;

--parādīt visus kursus un studentus, kas tajos pierakstīti
SELECT 
    kursi.nosaukums AS Kursa_nosaukums,
    studenti.vards || ' ' || studenti.uzvards AS students
FROM kursi
JOIN studentu_kursi ON kursi.kursa_id=studentu_kursi.kursa_id
JOIN studenti ON studentu_kursi.studenta_id=studenti.studenti_id
ORDER BY kursi.nosaukums;


--saskaitīt, cik studentu ir katrā kursā (parādīt st. skaitu un kursa.nosauk)
SELECT
    kursi.nosaukums AS Kursa_nosaukums,
    COUNT(studentu_kursi.studenta_id) AS Studentu_skaits
FROM kursi
LEFT JOIN studentu_kursi ON kursi.kursa_id = studentu_kursi.kursa_id
GROUP BY kursi.nosaukums;

--katram kursam parādīt vidējo atzīmi un studentu skaitu (kursa nos, atzime, skaits)
SELECT 
    kursi.nosaukums AS Kursa_nosaukums,
    COUNT(atzimes.studenta_id) AS Studentu_skaits,
    ROUND(AVG(atzimes.atzime),2) AS Videja_atzime
FROM kursi
LEFT JOIN atzimes ON kursi.kursa_id=atzimes.kursa_id
GROUP BY Kursa_nosaukums;

--parādīt katra studenta vidējo atzīmi(vārds, atzīme)
SELECT
    studenti.vards || ' ' || studenti.uzvards AS Students,
    ROUND(AVG(atzimes.atzime),2) AS Videja_atzime
FROM studenti
JOIN atzimes ON studenti.studenti_id = atzimes.studenta_id
GROUP BY studenti.studenti_id
ORDER BY Videja_Atzime DESC;