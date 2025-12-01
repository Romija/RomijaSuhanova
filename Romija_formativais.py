import sqlite3

savienojums = sqlite3.connect("Romija_sports.db")
cursor = savienojums.cursor()

#sportistu tabulas izveide
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sportisti(
        sportisti_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
)
""")

#nodarbības tabulu izveide
cursor.execute("""
    CREATE TABLE IF NOT EXISTS nodarbibas(
        nodarbibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sportisti_id TEXT NOT NULL,
        veids TEXT NOT NULL,
        ilgums_min INTEGER NOT NULL,
        FOREIGN KEY (sportisti_id) REFERENCES sportisti(sportisti_id)
)
""")

#pārbaude, vai lietotājs vēlas turpināt
def ievade_jn(teksts):
    while True:
        atbilde=input(teksts).lower()
        if atbilde in ["j","n"]:
            return atbilde
        print("Ievadi tikai j vai n!")

#pārbaude, vai lietotājs neatstāj tukšumu
def tuksa_ievade(teksts):
    while True:
        atbilde=input(teksts)
        if atbilde=="":
            print("Nav datu")
        else:
            return atbilde


#sportista pievienošana
while True:
    print("Pievienot sportistu: ")
    vards=tuksa_ievade("Ievadi vārdu: ")
    uzvards=tuksa_ievade("Ievadi uzvārdu: ")
    while True: #pārbaude vecumam
        try:
            vecums = int(tuksa_ievade("Ievadi sportista vecumu: "))
            if vecums>0:
                break
            else:
                print("Ievadi pozitīvu skaitli!")
        except ValueError:
            print("Ievadi skaitli!")

    #ieraksta datu bāzē
    cursor.execute("""
        INSERT INTO sportisti(vards, uzvards, vecums) VALUES(?,?,?)""",
        (vards, uzvards, vecums))
    savienojums.commit()
    turpinat = ievade_jn("Vai pievienot vēl sportistu? j/n: ")
    if turpinat =="n":
        break
print("Klients pievienots!")

#nodarbības pievienošana
while True:
    print("Pievieno nodarbību: ")
    while True: #id pārbaude
        try:
            sportisti_id=int(tuksa_ievade("Ievadi sportista id: "))
            cursor.execute("SELECT COUNT(*) FROM sportisti WHERE sportisti_id=?",(sportisti_id,))
            if cursor.fetchone()[0] >0:
                break
            else:
                print("Sportists ar šādu id neeksistē!")
        except ValueError:
            print("Ievadi skaitli, jo id ir cipars")

    veids = tuksa_ievade("Ievadi nodarbības veidu: ")

    #ilguma pārbaude
    while True:
        try:
            ilgums_min = int(tuksa_ievade("Ievadi ilgumu minūtēs: "))
            if ilgums_min>0:
                break
            else:
                print("Ievadi pozitīvu skaitli!")
        except ValueError:
            print("Ievadi skaitli!")
    #ieraksta datu bāzē
    cursor.execute("""
    INSERT INTO nodarbibas(sportisti_id, veids, ilgums_min) VALUES (?,?,?)
    """, (sportisti_id, veids, ilgums_min))
    savienojums.commit()
    turpinat = ievade_jn("Vai pievienot vēl nodarbību? j/n: ")
    if turpinat =="n":
        break


#vaicājumi
#Nr.1
cursor.execute("""
                SELECT sportisti.vards, sportisti.uzvards, COUNT(nodarbibas.nodarbibas_id) AS Skaits
                FROM sportisti
                JOIN nodarbibas ON sportisti.sportisti_id=nodarbibas.sportisti_id
                GROUP BY sportisti.sportisti_id
                """)
for rinda in cursor.fetchall():
    print(rinda)

#Nr.2
print("\n2. Kuri sportisti trenējās vairāk par 120minūtēm:")
cursor.execute("""
                SELECT sportisti.vards, sportisti.uzvards, SUM(nodarbibas.ilgums_min) as kopa_min
                FROM sportisti
                JOIN nodarbibas ON sportisti.sportisti_id=nodarbibas.sportisti_id
                HAVING kopa_min>120
                """)
for rinda in cursor.fetchall():
    print(rinda)