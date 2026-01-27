import flet as ft
import sqlite3


def main(page: ft.Page):
    page.title="TV šovi:datubāze"

    #savienojums ar datubāzi
    savienojums=sqlite3.connect("testa_dati_tv_sovi.db")
    cursor=savienojums.cursor()
    
    #teksts statusam(vai visi dati ievaditi)
    statuss=ft.Text("")
    
    #lauki datu ievadei
    lauks_nosaukums=ft.TextField(label="Nosaukums")
    lauks_kanals = ft.TextField(label="Kanāls")
    lauks_zanrs = ft.TextField(label="Žanrs")
    lauks_gads = ft.TextField(label="Gads")
    #funkcija datu saglabāšanai
    
    def saglabat(_): #nolasit ievadītas vērtības
        nosaukums=lauks_nosaukums.value.strip()
        kanals=lauks_kanals.value.strip()
        zanrs=lauks_zanrs.value.strip()
        gads_txt=lauks_gads.value.strip()
        
        if "" in [nosaukums,kanals,zanrs,gads_txt]:
            statuss.value="Kļūda: aizpildi visus laukus!"
        else:
            cursor.execute(
                """
                INSERT INTO televizijas_sovi(nosaukums,kanals,zanrs,gads)
                VALUES(?,?,?,?)
                """, 
                (nosaukums,kanals,zanrs,gads_txt)
            )
            savienojums.commit()
            statuss.value="Dati pievienoti!"
            
            #jānotīra ievades lauki
            lauks_nosaukums.value = ""
            lauks_kanals.value = ""
            lauks_zanrs.value = ""
            lauks_gads.value = ""   
        page.update()  #atjaunina statusu
    poga=ft.ElevatedButton("Saglabāt datus",on_click=saglabat)
    

    dal_vards = ft.TextField(label="Vārds")
    dal_uzvards = ft.TextField(label="Uzvārds")
    dal_profesija = ft.TextField(label="Profesija")

    #dropdown dati
    dd_dalibnieks=ft.Dropdown(label="Izvēlies dalībnieku",width=400)
    dd_sovs = ft.Dropdown(label="Izvēlies šovu",width=400)
    lauks_loma=ft.TextField(label="loma(vadītājs, dalībnieks/žūrija")

    def ieladet_dropdownus(): 
        #dalībnieki: id+vards+uzvards+profesija
        cursor.execute("""
            SELECT sovu_dalibnieki_id, vards, uzvards, profesija
            FROM sovu_dalibnieki
            ORDER BY uzvards, vards
            """
            )
        dal=cursor.fetchall()
        dd_dalibnieks.options=[
            ft.dropdown.Option(
                key=str(r[0]),
                text =f"{r[1]}({r[2]},{r[3]})"
            )
            for r in dal
        ]

        #šovu dati dropdownam: id+nosaukums(kanāls,gads)
        cursor.execute("""
            SELECT televizijas_sovi_id, nosaukums, kanals, gads
            FROM televizijas_sovi
            ORDER BY nosaukums
            """)
        sovi = cursor.fetchall()
        options = []
        for r in sovi:
            options.append(
                ft.dropdown.Option(
                key=str(r[0]),
                text =f"{r[1]}({r[2]},{r[3]})"
        )
        )
        dd_sovs.options = options #lai nav tukšs dropdown
        page.update() #lai dropwonam visuāli atjaunojas
    #lai dropwon uzreiz ielādē
    ieladet_dropdownus()

    def saglabat_dalibu(_):
        dal_id = dd_dalibnieks.value
        sova_id = dd_sovs.value
        loma = lauks_loma.value.strip()

        if dal_id is None or sova_id is None or loma=="":
            statuss.value = "Jāaizpilda visi laiku!"
            page.update()
            return

        cursor.execute("""
            INSERT INTO sovu_dalibas(sovu_dalibnieki_id, televizijas_sovi_id, loma)
            VALUES(?,?,?)
            """,
            (int(dal_id), int(sova_id),loma)
            )
        savienojums.commit()
        statuss.value = "Dalība pievienota!"
        lauks_loma.value=""
        page.update()

    def saglabat_dalibnieku(e):
        vards = dal_vards.value.strip()
        uzvards = dal_uzvards.value.strip()
        profesija = dal_profesija.value.strip()
    
        if "" in [vards, uzvards, profesija]:
            statuss.value = "Kļūda: aizpildi visus dalībnieka laukus!"
        else:
            cursor.execute(
                """
                INSERT INTO sovu_dalibnieki (vards, uzvards, profesija)
                VALUES (?, ?, ?)
                """,
                (vards, uzvards, profesija)
            )
            savienojums.commit()

            statuss.value = "Dalībnieks pievienots!"
            dal_vards.value = ""
            dal_uzvards.value = ""
            dal_profesija.value = ""
            
            page.update()
    poga_dalibnieks = ft.ElevatedButton("Saglabāt dalībnieku", on_click=saglabat_dalibnieku)
    poga_daliba=ft.ElevatedButton("Saglabāt dalību",on_click=saglabat_dalibu)
    page.add(lauks_nosaukums,
             lauks_kanals,
             lauks_zanrs,
             lauks_gads,
             poga,
             ft.Text("Dalībnieka pievienošana"),
             dal_vards,
             dal_uzvards,
             dal_profesija,
             poga_dalibnieks,
             ft.Text("Dalības pievienošana"),
             dd_dalibnieks,
             dd_sovs,
             lauks_loma,
             poga_daliba,
             statuss)

ft.app(target=main)    
