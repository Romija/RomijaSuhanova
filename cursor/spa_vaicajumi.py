#pieslēgties esošajai datubāzei
#jāuzraksta programma, kur lietotājs var izvēlēties opcijas no 0-5
#katra opcija atgriež vaicājuma rezultātus, bet 0 - exit
#nevar ievadīt neko citu kā tikai 0-5
#1-visi klienti
#2-visi pakalpojumi
#3-visi pieraksti(ar klienta vārdu un pakalpojuma nosaukumu)
#4-tuvāko 7 dienu pieraksti
#5-lietotājs norāda cenu, parādīt pakalpojumus, kas ir dārgāki par norādīto
import sqlite3
savienojums = sqlite3.connect("spa_sistema.db")
cursor = savienojums.cursor()

print("Izvēles:\n0-iziet no programmas\n1-visi klienti\n2-visi pakalpojumi\n3-visi pieraksti(ar klienta vārdu un pakalpojuma nosaukumu)\n4-tuvāko 7 dienu pieraksti\n5-lietotājs norāda cenu, parādīt pakalpojumus, kas ir dārgāki par norādīto")
while True:
    try:

        izvele = int(input("Ievadi savu izvēli (0-5): "))

        if izvele == 0:
            print("Programma beidzas!")
            exit()

        elif izvele ==  1:
            print('Visi klienti: ')
            cursor.execute("""
                SELECT*FROM klienti
                ORDER BY klienti.uzvards ASC
                """)
            dati = cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]}:{rinda[1]} {rinda[2]},telefons {rinda[3]}")
            else:
                print("Datu bāzē nav klientu")

        elif izvele == 2:
            print('Visi pakalpojumi: ')
            cursor.execute("SELECT*FROM pakalpojumi")
            for rinda in cursor.fetchall():
                print(rinda)

        elif izvele == 3:
            print('Visi pieraksti: ')
            cursor.execute("""
                SELECT pieraksti.pieraksti_id,
                    klienti.vards ||' '|| klienti.uzvards AS klients,
                    pakalpojumi.nosaukums AS Pakalpojums,
                    pakalpojumi.cena,
                    pieraksti.datums
                FROM pieraksti
                JOIN klienti ON pieraksti.klients_id=klienti.klienti_id
                JOIN pakalpojumi ON pieraksti.pakalpojums_id=pakalpojumi.pakalpojumi_id
                ORDER BY pieraksti.datums ASC
                """)
            dati = cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]}:{rinda[1]} {rinda[2]}, {rinda[3]}, {rinda[4]}")
            else:
                print("Datu bāzē nav klientu")
        
        elif izvele == 4:
            print("Pieraksti tuvāko 7 dienu laikā")
            cursor.execute("""
                SELECT klienti.vards ||' '|| klienti.uzvards AS klients,
                    pakalpojumi.nosaukums AS Pakalpojums,
                    pieraksti.datums
                FROM pieraksti
                    JOIN klienti ON pieraksti.klients_id=klienti.klienti_id
                    JOIN pakalpojumi ON pieraksti.pakalpojums_id=pakalpojumi.pakalpojumi_id
                    WHERE pieraksti.datums BETWEEN date('now') AND date('now','+7 days')
                    ORDER BY pieraksti.datums ASC
            """)
            dati = cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]}:{rinda[1]} {rinda[2]}")
            else:
                print("Datu bāzē nav klientu")
        
        elif izvele == 5:
            while True:
                try:
                    slieksnis = float(input("Ievadi minimālo cenu: "))
                    if slieksnis<=0:
                        print("Ievadi pareizi")
                        continue
                    break
                except ValueError:
                    print("Lūdzu ievadi skaitli!")

            cursor.execute("""
            SELECT pakalpojumi.nosaukums, pakalpojumi.ilgums, pakalpojumi.cena
            FROM pakalpojumi
            WHERE pakalpojumi.cena>?
            ORDER BY pakalpojumi.cena DESC
            """,(slieksnis,))

            dati = cursor.fetchall()
            if dati:
                for rinda in dati:
                    print(f"ID {rinda[0]}:{rinda[1]} {rinda[2]}")
            else:
                print("Nav")

        else:
            print("Ievadi skaitli no 0 līdz 5!")

    except ValueError:
        print("Ievadi skaitli!")

