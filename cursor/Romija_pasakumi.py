import sqlite3
from datetime import datetime

savienojums = sqlite3.connect("Romija_datubaze.db")
cursor = savienojums.cursor()

#tabulu izveide
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pasakumi(
        pasakumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        datums TEXT NOT NULL,
        vieta TEXT NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS dalibnieki(
        dalibnieki_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS registracijas(
        registracijas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pasakumi_id INTEGER NOT NULL,
        dalibnieki_id INTEGER NOT NULL,
        statuss TEXT NOT NULL,
        FOREIGN KEY (pasakumi_id) REFERENCES pasakumi(pasakumi_id)
        FOREIGN KEY (dalibnieki_id) REFERENCES dalibnieki(dalibnieki_id)
)
""")

#funkcija, kas pārbauda, vai skaitlis ir korekti ievadīts
def ievadi_skaitli(skaitlis):
    while True:
        try:
            sk=int(input(skaitlis))
            return sk
        except ValueError:
            print("Jāievada vesels skaitlis")

#funkcija, kas pārbauda, vai dalībnieka id eksistē
def dalibnieka_id_eksiste(dalibnieki_id):
    cursor.execute("""
        SELECT COUNT(*) FROM dalibnieki WHERE dalibnieki_id=?
        """, (dalibnieki_id,))
    return cursor.fetchone()[0]>0

#funkcija, kas pārbauda, vai pasākuma id eksistē
def pasakuma_id_eksiste(pasakumi_id):
    cursor.execute("""
        SELECT COUNT(*) FROM dalibnieki WHERE dalibnieki_id=?
        """, (pasakumi_id,))
    return cursor.fetchone()[0]>0

#funkcija, kas pārbauda, vai lietotājs vēlas turpināt
def ievade_jn(teksts):
    while True:
        atbilde=input(teksts).lower()
        if atbilde in ["j","n"]:
            return atbilde
        print("Ievadi tikai j vai n!")

#pievieno pasākumus
while True:
    pasakumu_skaits=0
    print("Pievieno pasākumu: ")
    while pasakumu_skaits<2:
        nosaukums = input("Ievadi pasākuma nosaukumu: ")
        #datuma pārbaude
        while True:
            datums_txt = input("Ievadi pasākuma datumu (YYYY-MM-DD): ")
            try:
                datums = datetime.strptime(datums_txt, "%Y-%m-%d").date()
                if datums<datetime.now().date():
                    print("Datums nevar būt pagātnē!")
                else:
                    break
            except ValueError:
                print("Nepareizs formāts")
        vieta = input("Ievadi pasākuma vietu: ")
        cursor.execute("""INSERT INTO pasakumi(nosaukums,datums,vieta)
                        VALUES(?,?,?)
                        """,(nosaukums, str(datums),vieta))
        savienojums.commit()
        pasakumu_skaits+=1
        print("Pasākums pievienots!")
    turpinat = ievade_jn("Vai pievienot vēl pasākumu? j/n: ")
    if turpinat =="n":
        break

#pievieno dalībniekus
while True:
    dalib_skaits = 0
    print("Pievieno dalībnieku: ")
    while dalib_skaits<2:
        vards = input("Ievadi dalībnieka vārdu: ")
        uzvards = input("Ievadi dalībnieka uzvārdu: ")
        #pārbauda vecumu
        while True:
            try:
                vecums = int(input("Ievadi dalībnieka vecumu: "))
                if vecums>0:
                    break
                else:
                    print("Ievadi pozitīvu skaitli!")
            except ValueError:
                print("Ievadi skaitli!")
        cursor.execute("""INSERT INTO dalibnieki(vards,uzvards,vecums)
                        VALUES(?,?,?)
                        """,(vards, uzvards,vecums))
        savienojums.commit()
        dalib_skaits+=1
        print("Dalībnieks pievienots!")
    turpinat = ievade_jn("Vai pievienot vēl dalībnieku? j/n: ")
    if turpinat =="n":
        break

#pievieno reģistrāciju
while True:
    reg_skaits=0
    print("Pievieno reģistrāciju: ")
    while reg_skaits<2:
        while True:
            pasakumi_id = ievadi_skaitli("Ievadi pasākuma id: ")
            if pasakuma_id_eksiste(pasakumi_id):
                break
            else:
                print("Tāds id neeksistē")
        while True:
            dalibnieki_id = ievadi_skaitli("Ievadi dalībnieka id: ")
            if dalibnieka_id_eksiste(dalibnieki_id):
                break
            else:
                print("Tāds id neeksistē")
        statuss = input("Ievadi statusu (jā/nē): ")
        cursor.execute("""INSERT INTO registracijas(pasakumi_id,dalibnieki_id,statuss)
                        VALUES(?,?,?)
                        """,(pasakumi_id, dalibnieki_id,statuss))
        savienojums.commit()
        reg_skaits+=1
        print("Reģistrācija pievienota!")
    turpinat = ievade_jn("Vai pievienot vēl reģistrāciju? j/n: ")
    if turpinat =="n":
        break

#parādīt visus pasākumus
cursor.execute("""
    SELECT * FROM pasakumi""")
rezultati=cursor.fetchall()
print("\nVisi pasākumi: ")
for r in rezultati:
    print(f"{r[1]} {r[2]} {r[3]}")

#parādīt dalībniekus, kas vecāki par 17 gadiem
cursor.execute("""
    SELECT * FROM dalibnieki WHERE vecums>17""")
rezultati=cursor.fetchall()
print("\nDalībnieki, kas vecāki par 17 gadiem: ")
for r in rezultati:
    print(f"{r[1]} {r[2]}, vecums: {r[3]}")

#kurš dalībnieks kurā pasākumā būs
cursor.execute("""
    SELECT dalibnieki.vards,
        dalibnieki.uzvards,
        pasakumi.nosaukums
    FROM registracijas
    LEFT JOIN dalibnieki ON dalibnieki.dalibnieki_id=registracijas.dalibnieki_id
    LEFT JOIN pasakumi ON pasakumi.pasakumi_id=registracijas.pasakumi_id""")
rezultati=cursor.fetchall()
print("\nKurš dalībnieks, kur piedalās: ")
for r in rezultati:
    print(f"{r[0]} {r[1]} piedalīsies: {r[2]}")

#dalībnieku skaits katrā pasākumā
cursor.execute("""
    SELECT pasakumi.nosaukums,
        COUNT(registracijas.dalibnieki_id) AS Skaits
    FROM registracijas
    RIGHT JOIN dalibnieki ON dalibnieki.dalibnieki_id=registracijas.dalibnieki_id
    RIGHT JOIN pasakumi ON pasakumi.pasakumi_id=registracijas.pasakumi_id
    GROUP BY pasakumi.nosaukums""")
rezultati=cursor.fetchall()
print("\nDalībnieku skaits katrā pasākumā")
for r in rezultati:
    print(f"{r[0]}, dalībnieku skaits: {r[1]}")

#uz kuriem pasākumiem vairāk kā 3 cilvēki pieteikušies
cursor.execute("""
    SELECT pasakumi.nosaukums,
        COUNT(registracijas.dalibnieki_id) AS skaits
    FROM registracijas
    LEFT JOIN dalibnieki ON dalibnieki.dalibnieki_id=registracijas.dalibnieki_id
    LEFT JOIN pasakumi ON pasakumi.pasakumi_id=registracijas.pasakumi_id
    GROUP BY pasakumi.nosaukums
    HAVING skaits>3""")
rezultati=cursor.fetchall()
print("\nPasākumi, kuros ir pieteikušies vairāk par 3 cilvēkiem: ")
for r in rezultati:
    print(f"{r[0]}, dalībnieku skaits: {r[1]}")

#izdomātais vaicājums - pasākumi, kuros nav pieteikušies dalībnieki
cursor.execute("""
    SELECT pasakumi.nosaukums,
        COUNT(registracijas.dalibnieki_id) AS skaits
    FROM registracijas
    RIGHT JOIN dalibnieki ON dalibnieki.dalibnieki_id=registracijas.dalibnieki_id
    RIGHT JOIN pasakumi ON pasakumi.pasakumi_id=registracijas.pasakumi_id
    GROUP BY pasakumi.nosaukums
    HAVING skaits<1""")
rezultati=cursor.fetchall()
print("\nPasākumi, kuros nav pieteikušies cilvēki: ")
for r in rezultati:
    print(f"{r[0]}, dalībnieku skaits: {r[1]}")
