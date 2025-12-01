import sqlite3
savienojums=sqlite3.connect("skola_trenins.db") #automātiski izveido failu, ja tāda nav

#cursor objektu
cursor=savienojums.cursor()
cursor.execute("DROP TABLE IF EXISTS skoleni") #lai testa dati nedublētos

#izveidot tabulu skolēni ar kollonām id, vards, vecums
cursor.execute("""
    CREATE TABLE IF NOT EXISTS skoleni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        vecums INTEGER NOT NULL
    )
""")

cursor.execute("INSERT INTO skoleni(vards,vecums) VALUES (?,?)",("Anna",15))
cursor.execute("INSERT INTO skoleni(vards,vecums) VALUES (?,?)",("Jānis",17))
cursor.execute("INSERT INTO skoleni(vards,vecums) VALUES (?,?)",("Gunārs",16))

savienojums.commit() #ievieto datus datubāzē

print("Visi skolēni: ")
cursor.execute("SELECT*FROM skoleni")
visi=cursor.fetchall()
for i in visi:
    print(f"ID:{i[0]} | Vārds:{i[1]} | Vecums:{i[2]}")

print("\nSkolēni, kas jaunāki par noteiktu vecumu: ")
cursor.execute("SELECT*FROM skoleni WHERE vecums < 16")
jaunie=cursor.fetchall()
for i in jaunie:
    print(f"{i[1]} ({i[2]} gadi)")

#vecākais skolēns
cursor.execute("SELECT*FROM SKOLENI ORDER BY VECUMS desc limit 1")
vecakais=cursor.fetchone()
print(f"\nVecākais skolēns: {vecakais[1]} ({vecakais[2]} gadi)")

#saskaitīt skolēnus, kuri jaunāki par 17 gadiem
cursor.execute("SELECT COUNT(*) FROM skoleni WHERE vecums <17")
rez = cursor.fetchone()[0] #jo vajag tikai 1 konkrētu vērtību
print(f"Jaunāki par 17 gadiem: {rez}")
