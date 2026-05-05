import requests
import sqlite3

#1.solis - pieslēgšanās datubāzei
savienojums = sqlite3.connect("catfacts.db")
cursor = savienojums.cursor()

#2.solis - Tabulas izveide
cursor.execute('''
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fact TEXT NOT NULL,
                lenght INTEGER
                )
        ''')

#3.solis - datu iegūšana 
#iegūst 10 faktus
for i in range(10):
    #nosūta pieprasījumu uz API adresi
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    #pārbauda, vai statusa kods ir veiksmīgs
    if response.status_code == 200:
        data = response.json() #json ir kā vārdnīca
        #saņemtod datus atgriež apmēram šādi:
        #{"fact" : "...", "lenght" : 123}
        #paņem konkrētas vērtības no vārdnīcas
        fact = data['fact']
        length = data['length']
        #4.solis - ielikt datubāzē
        cursor.execute('''
                INSERT INTO facts (fact, lenght) VALUES (?,?)''', (fact, length))

#datus saglabā un aizver db
savienojums.commit()
savienojums.close()
print('Fakti saglabāti datubāzē!')

