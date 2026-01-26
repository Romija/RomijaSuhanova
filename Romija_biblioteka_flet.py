import sqlite3
import flet as ft

savienojums = sqlite3.connect("biblioteka_Romija.db")
cursor = savienojums.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS gramatas(
        gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nosaukums TEXT NOT NULL,
        autors TEXT NOT NULL,
        gads INTEGER NOT NULL,
        zanrs TEXT NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS lasitaji(
        lasitaji_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        klase TEXT NOT NULL
)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS iznemtas_gramatas(
        iznemtas_gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
        gramatas_id INTEGER NOT NULL,
        lasitaji_id INTEGER NOT NULL,
        datums TEXT NOT NULL,
        atdots INTEGER NOT NULL,
        FOREIGN KEY (gramatas_id) REFERENCES gramatas(gramatas_id) ON DELETE CASCADE,
        FOREIGN KEY (lasitaji_id) REFERENCES lasitaji(lasitaji_id) ON DELETE CASCADE
)
""")

def main(page: ft.Page):
    page.title="Bibliotēkas datubāze"

    #savienojums ar datubāzi
    savienojums=sqlite3.connect("biblioteka_Romija.db")
    cursor=savienojums.cursor()
    
    #teksts statusam(vai visi dati ievaditi)
    statuss=ft.Text("")
    statuss2=ft.Text("")
    statuss3=ft.Text("")
    statuss4=ft.Text("")
    
    #lauki datu ievadei
    lauks_nosaukums=ft.TextField(label="Nosaukums")
    lauks_autors = ft.TextField(label="Autors")
    lauks_gads = ft.TextField(label="Gads")
    lauks_zanrs = ft.TextField(label="Žanrs")

    #funkcija datu saglabāšanai
    def pievienot_gramatu(_): #nolasit ievadītas vērtības
        nosaukums=lauks_nosaukums.value.strip()
        autors=lauks_autors.value.strip()
        gads=lauks_gads.value.strip()
        zanrs=lauks_zanrs.value.strip()

        if gads.isnumeric(): #pārbauda, vai skaitlis

            if "" in [nosaukums,autors,gads,zanrs]: #brīdina, ka viss jāizpilda
                statuss.value="Kļūda: aizpildi visus laukus!"

            else:
                cursor.execute(
                    """
                    INSERT INTO gramatas(nosaukums,autors,gads,zanrs)
                    VALUES(?,?,?,?)
                    """, 
                    (nosaukums,autors,gads,zanrs)
                )
                savienojums.commit()
                statuss.value="Dati pievienoti!"
                
                #jānotīra ievades lauki
                lauks_nosaukums.value = ""
                lauks_autors.value = ""
                lauks_gads.value = ""
                lauks_zanrs.value = ""   
        else:
            statuss2.value = "Kļūda: Gadam ir jābūt skaitlim!"

        page.update()  #atjaunina statusu
        
    poga=ft.ElevatedButton("Saglabāt grāmatu",on_click=pievienot_gramatu)

    #lauki datu ievadei
    lauks_vards=ft.TextField(label="Vards")
    lauks_uzvards = ft.TextField(label="Uzvārds")
    lauks_klase = ft.TextField(label="Klase")
    
    def pievienot_lasitaju(_): #nolasit ievadītas vērtības
        vards=lauks_vards.value.strip()
        uzvards=lauks_uzvards.value.strip()
        klase=lauks_klase.value.strip()

        if "" in [vards,uzvards,klase]: #brīdina, ka viss jāizpilda
            statuss.value="Kļūda: aizpildi visus laukus!"

        else:
            cursor.execute(
                """
                INSERT INTO lasitaji(vards,uzvards,klase)
                VALUES(?,?,?)
                """, 
                (vards,uzvards,klase)
            )
            savienojums.commit()
            statuss3.value="Dati pievienoti!"
            
            #jānotīra ievades lauki
            lauks_vards.value = ""
            lauks_uzvards.value = ""
            lauks_klase.value = ""

        page.update()  #atjaunina statusu
        
    poga_lasitaji=ft.ElevatedButton("Saglabāt lasītāju",on_click=pievienot_lasitaju)

    #dropdown dati
    dd_gramata=ft.Dropdown(label="Izvēlies grāmatu",width=400)
    dd_lasitajs=ft.Dropdown(label="Izvēlies lasītāju",width=400)
    lauks_datums = ft.TextField(label="Datums")
    lauks_atdots = ft.TextField(label="Atdots")

    def ieladet_dropdownus():
        cursor.execute("""
            SELECT gramatas_id, nosaukums, autors, gads, zanrs
            FROM gramatas
            ORDER BY nosaukums
            """
            )
        dal=cursor.fetchall()
        dd_gramata.options=[
            ft.dropdown.Option(
                key=str(r[0]),
                text =f"{r[1]}({r[2]},{r[3]},{r[4]})"
            )
            for r in dal
        ]

        cursor.execute("""
            SELECT lasitaji_id, vards, uzvards, klase
            FROM lasitaji
            ORDER BY vards
            """)
        lasitaji = cursor.fetchall()
        options = []
        for r in lasitaji:
            options.append(
                ft.dropdown.Option(
                key=str(r[0]),
                text =f"{r[1]}({r[2]},{r[3]})"
        )
        )
        dd_lasitajs.options = options #lai nav tukšs dropdown
        page.update() #lai dropwonam visuāli atjaunojas
    #lai dropwon uzreiz ielādē
    ieladet_dropdownus()

    def registret(_):
        gramatas_id = dd_gramata.value
        lasitaji_id = dd_lasitajs.value
        datums = lauks_datums.value.strip()
        atdots = lauks_atdots.value.strip()

        if gramatas_id is None or lasitaji_id is None or datums=="" or atdots=="":
            statuss.value = "Jāaizpilda visi laiku!"
            page.update()
            return

        cursor.execute("""
            INSERT INTO iznemtas_gramatas(gramatas_id, lasitaji_id, datums, atdots)
            VALUES(?,?,?)
            """,
            (int(gramatas_id), int(lasitaji_id),datums, atdots)
            )
        savienojums.commit()
        statuss4.value = "Reģistrācija pievienota!"
        lauks_gads.value=""
        lauks_atdots.value=""
        page.update()
    poga_reg=ft.ElevatedButton("Saglabāt reģistrāciju",on_click=registret)

    #pievienoti visi elementi
    page.add(lauks_nosaukums,
                lauks_autors,
                lauks_gads,
                lauks_zanrs,
                poga,
                statuss,
                statuss2,
                ft.Text("Lasītāja pievienošana"),
                lauks_vards,
                lauks_uzvards,
                lauks_klase,
                poga_lasitaji,
                statuss3,
                dd_gramata,
                dd_lasitajs,
                lauks_datums,
                lauks_atdots,
                poga_reg,
                statuss4)

ft.app(target=main)