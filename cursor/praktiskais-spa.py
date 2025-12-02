import sqlite3
from datetime import datetime

savienojums = sqlite3.connect("spa_sistema.db")
cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS klienti(
        klienti_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        telefons TEXT NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pakalpojumi(
        pakalpojumi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        ilgums INTEGER NOT NULL,
        cena REAL NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pieraksti(
        pieraksti_id INTEGER PRIMARY KEY AUTOINCREMENT,
        klients_id TEXT NOT NULL,
        pakalpojums_id TEXT NOT NULL,
        datums TEXT NOT NULL,
        FOREIGN KEY (klients_id) REFERENCES klienti(klienti_id),
        FOREIGN KEY (pakalpojums_id) REFERENCES pakalpojumi(pakalpojumi_id)
)
""")
def ievade_jn(teksts):
    while True:
        atbilde=input(teksts).lower()
        if atbilde in ["j","n"]:
            return atbilde
        print("Ievadi tikai j vai n!")


#tabula klienti
while True:
    print("Pievienot klientu: ")
    vards=input("Ievadi vārdu: ")
    uzvards=input("Ievadi uzvārdu: ")
    telefons=input("Ievadi telefona nr: ")

    cursor.execute("""
        INSERT INTO klienti(vards, uzvards, telefons) VALUES(?,?,?)""",
        (vards, uzvards, telefons))
    savienojums.commit()
    turpinat = ievade_jn("Vai pievienot vēl klientu? j/n: ")
    if turpinat =="n":
        break

print("Klients pievienots!")



#tabula pakalpojumi
while True:
    print("Pievieno pakalpojumu: ")
    nosaukums=input("Ievadi pakalpojuma nosaukumu: ")
    while True:
        try:
            ilgums = int(input("Ievadi pakalpojuma ilgumu: "))
            if ilgums>0:
                break
            else:
                print("Ievadi pozitīvu skaitli!")
        except ValueError:
            print("Ievadi skaitli!")

    while True:
        try:
            cena = float(input("Ievadi pakalpojuma cenu: "))
            if cena>0:
                break
            else:
                print("Ievadi pozitīvu skaitli!")
        except ValueError:
            print("Ievadi skaitli!")
    

    cursor.execute("""
        INSERT INTO pakalpojumi(nosaukums, ilgums, cena) VALUES (?,?,?)
        """, (nosaukums, ilgums, cena))
    savienojums.commit()
    turpinat = ievade_jn("Vai pievienot vēl pakalpojumu? j/n: ")
    if turpinat =="n":
        break

#pārbaudīt kādi klienti(un id) jau eksistē
while True:
    print("Pieejamie klienti: ")
    cursor.execute("SELECT klienti_id,vards,uzvards FROM klienti")
    for klients in cursor.fetchall():
        print(f"ID {klients[0]} - {klients[1]} - {klients[2]}")

    #pārbaudīt, vai klienta id tabulā eksistē
    while True:
        try:
            klients_id=int(input("Ievadi klienta id: "))
            #klienta ievade ar id pārbaudi
            cursor.execute("SELECT COUNT(*) FROM klienti WHERE klienti_id=?",(klients_id,))
            if cursor.fetchone()[0] >0:
                break #id pareizs - turpina
            else:
                print("Klients ar šādu id neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo id ir cipars")

    #apskatīt pieejamos pakalpojumus
    print("\nPieejamie pakalpojumi: ")
    cursor.execute("SELECT pakalpojumi_id, nosaukums, cena FROM pakalpojumi")
    for p in cursor.fetchall():
        print(f"ID {p[0]} - {p[1]} ({p[2]} eiro)")
    #pakalpojumu id pārbaude
    while True:
        try:
            pakalpojums_id=int(input("Ievadi pakalpojuma id: "))
            #Pārbaudīt, vai pakalpojuma id tabulā eksistē
            cursor.execute("SELECT COUNT(*) FROM pakalpojumi WHERE pakalpojumi_id=?",(pakalpojums_id,))
            if cursor.fetchone()[0] >0:
                break #id pareizs - turpina
            else:
                print("Pakalpojums ar šādu id neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo id ir cipars")
    #ja abi ir pareizi, tad jautā datumu un ieraksta datus tabulā
    while True:
        datums_txt=input("Ievadi datumu: ")
        try:
            datums = datetime.strptime(datums_txt, "%Y-%m-%d").date()
            if datums<datetime.now().date():
                print("Datums nevar būt pagātnē!")
            else:
                break
        except ValueError:
            print("Nepareizs formāts")
    cursor.execute("""
    INSERT INTO pieraksti(klients_id, pakalpojums_id, datums) VALUES (?,?,?)
    """, (klients_id, pakalpojums_id, str(datums)))
    savienojums.commit()
    turpinat = ievade_jn("Vai pievienot vēl pierakstu? j/n: ")
    if turpinat =="n":
        break



'''
#tabula pieraksti
while True:
    print("Pievieno pierakstu: ")
    klients_id = int(input("Ievadi klienta ID: "))
    pakalpojums_id = int(input("Ievadi pakalpojuma ID: "))
    datums = input("Ievadi pieraksta datumu (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO pieraksti(klients_id, pakalpojums_id, datums) VALUES (?,?,?)
        """, (klients_id, pakalpojums_id, datums))
    savienojums.commit()
    turpinat = input("Vai pievienot vēl pierakstu? j/n: ".lower())
    if turpinat !="j":
        break
'''

#parādīt tabulā esošos datus
print('Visi apmeklētāji: ')
cursor.execute("SELECT*FROM klienti")
for rinda in cursor.fetchall():
    print(rinda)

print('Visi pakalpojumi: ')
print("Tabula: pakalpojumi-----")
cursor.execute("SELECT*FROM pakalpojumi")
for rinda in cursor.fetchall():
    print(rinda)

print('Visi pieraksti: ')
cursor.execute("SELECT*FROM pieraksti")
for rinda in cursor.fetchall():
    print(rinda)

