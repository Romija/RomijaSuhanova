import sqlite3

savienojums = sqlite3.connect("formativais_labojums.db")
cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sportisti(
        sportisti_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        vecums INTEGER NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nodarbibas(
        nodarbibas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sportisti_id INTEGER NOT NULL,
        veids TEXT NOT NULL,
        ilgums_min INTEGER NOT NULL,
        FOREIGN KEY (sportisti_id) REFERENCES sportisti(sportisti_id)
)
""")

#papildfunkcijas datu pārbaudei (lai nav tukšs teksts, lai ir skaitlis un lai eksistē id)
#pārbaude, vai lietotājs neatstāj tukšumu
def ievadi_tekstu(teksts):
    while True:
        atbilde=input(teksts).strip()
        if atbilde=="":
            print("Nav datu")
        else:
            return atbilde

#skaitļu pārbaude            
def ievadi_skaitli(skaitlis):
    while True:
        try:
            sk=int(input(skaitlis))
            return sk
        except ValueError:
            print("Jāievada vesels skaitlis")

#pārbauda, vai id eksistē
def sportista_id_eksiste(sportista_id):
    cursor.execute("""
        SELECT COUNT(*) FROM sportisti WHERE sportisti_id=?
        """, (sportista_id,))
    return cursor.fetchone()[0]>0

#sportistu pievienošana

sportistu_skaits=0
while sportistu_skaits<=5:
    vards=ievadi_tekstu("Ievadi sportista vārdu: ")
    uzvards=ievadi_tekstu("Ievadi sportista uzvārdu: ")
    vecums=ievadi_skaitli("Ievadi sportista vecumu: ")

    cursor.execute("""INSERT INTO sportisti(vards,uzvards,vecums)
                    VALUES(?,?,?)
                    """,(vards, uzvards,vecums))
    savienojums.commit()
    sportistu_skaits+=1
    print("Sportists pievienots\n")

nodarbibu_skaits=0
while nodarbibu_skaits<=5:
    while True:
        sportisti_id = ievadi_skaitli("Ievadi sportista id: ")
        if sportista_id_eksiste(sportisti_id):
            break
        else:
            print("Tāds id neeksistē")
    veids = ievadi_tekstu("Ievadi nodarbības veidu: ")
    ilgums_min = ievadi_skaitli("Ievadi ilgumu minūtēs: ")

    cursor.execute("""INSERT INTO nodarbibas(sportisti_id,veids,ilgums_min)
                    VALUES(?,?,?)
                    """,(sportisti_id, veids,ilgums_min))
    savienojums.commit()
    nodarbibu_skaits+=1
    print("Nodarbība pievienota\n")

#Parādīt katra sportista kopējo nodarbību skaitu
cursor.execute("""
    SELECT sportisti.vards,
        sportisti.uzvards,
        COUNT(nodarbibas.nodarbibas_id) AS Skaits
    FROM sportisti
    LEFT JOIN nodarbibas ON sportisti.sportisti_id=nodarbibas.sportisti_id
    GROUP BY sportisti.sportisti_id""")
rezultati=cursor.fetchall()
for r in rezultati:
    print(f"{r[0]} {r[1]}-nodarbību skaits: {r[2]}")

#sportisti, kuri trenējušies vairāk kā 120min
cursor.execute("""
    SELECT sportisti.vards,
        sportisti.uzvards,
        SUM(nodarbibas.ilgums_min) AS kopa_min
    FROM sportisti
    JOIN nodarbibas ON sportisti.sportisti_id=nodarbibas.sportisti_id
    GROUP BY sportisti.sportisti_id
    HAVING kopa_min>120
    """)
rezultati=cursor.fetchall()
if len(rezultati)==0:
    print("Nav datu")
else:
    for r in rezultati:
        print(f"{r[0]} {r[1]}- ilgums minūtēs: {r[2]}")

#top 3 rezultāti pēc laika
cursor.execute("""
    SELECT sportisti.vards,
        sportisti.uzvards,
        SUM(nodarbibas.ilgums_min) AS kopa_min
    FROM sportisti
    LEFT JOIN nodarbibas ON sportisti.sportisti_id=nodarbibas.sportisti_id
    GROUP BY sportisti.sportisti_id
    ORDER BY kopa_min DESC
    LIMIT 3
    """)
rezultati=cursor.fetchall()
for r in rezultati:
        print(f"{r[0]} {r[1]}- ilgums minūtēs: {r[2]}")