import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "Bibliotēka"
    page.scroll=ft.ScrollMode.AUTO

    savienojums = sqlite3.connect("biblioteka_vards.db", check_same_thread=False)
    cursor = savienojums.cursor()
   

    #izveido tabulas, ja DB ir tukšs
    cursor.executescript( #executescript() ir paredzēts tieši DB struktūras izveidei
        """
        CREATE TABLE IF NOT EXISTS gramatas (
            gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nosaukums TEXT NOT NULL,
            autors TEXT NOT NULL,
            gads INTEGER NOT NULL,
            zanrs TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS lasitaji (
            lasitaji_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vards TEXT NOT NULL,
            uzvards TEXT NOT NULL,
            klase TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS iznemtas_gramatas (
            iznemtas_gramatas_id INTEGER PRIMARY KEY AUTOINCREMENT,
            gramatas_id INTEGER NOT NULL,
            lasitaji_id INTEGER NOT NULL,
            datums TEXT NOT NULL,
            atdots INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (gramatas_id) REFERENCES gramatas(gramatas_id),
            FOREIGN KEY (lasitaji_id) REFERENCES lasitaji(lasitaji_id)
        );
        """
    )
    savienojums.commit()
    statuss = ft.Text("")

    #logs rezultātiem
    rezultatu_dialogs = ft.AlertDialog(
        modal = True,
        title =ft.Text("Rezultāti"),
        content = ft.Text(""),
        actions = [ft.TextButton("Aizvērt")],
    )

    page.overlay.append(rezultatu_dialogs) #bez šī logs var neparādīties
    def aizvert_dialogu(_):
        rezultatu_dialogs.open=False
        page.update()
    #piesiet "aizvērt" pogai funkciju
    rezultatu_dialogs.actions=[ft.TextButton("Aizvērt", on_click=aizvert_dialogu)]

    def paradit_tabulu(virsraksts, kolonnas, rindas):
        #izveidot kolonnas
        datu_kolonnas = [] #nepieciešams kolonnām
        for k in kolonnas:
            kolonna=ft.DataColumn(ft.Text(k))
            datu_kolonnas.append(kolonna)

        datu_rindas=[]
        for rinda in rindas:
            cells=[] #šunai vienai rindai
            for vertiba in rinda:
                cell=ft.DataCell(ft.Text(vertiba))
                cells.append(cell)
            datu_rindas.append(ft.DataRow(cells=cells))
        
        #uztaisa tabulu
        tabula=ft.DataTable(
            columns=datu_kolonnas,
            rows=datu_rindas
        )

        #ieliek tabulu dialoglogā
        rezultatu_dialogs.title=ft.Text(virsraksts)
        rezultatu_dialogs.content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Rindu skaits: {len(rindas)}"),
                    ft.Divider(),
                    tabula
                ],
                    scroll=ft.ScrollMode.AUTO
            ),
            width=900,
            height=500
        )
        rezultatu_dialogs.open=True
        page.update()

    #dropdowni
    gramatu_izvele = ft.Dropdown(label="Izvēlies grāmatu", width=450)
    lasitaju_izvele = ft.Dropdown(label="Izvēlies lasītāju", width=450)

    def ieladet_dropdownus():
        try:
            cursor.execute(
                """
                SELECT gramatas_id, nosaukums, autors
                FROM gramatas
                ORDER BY nosaukums
                """
            )
            gramatas = cursor.fetchall()
            gramatu_izvele.options = [
                ft.dropdown.Option(key=str(r[0]), text=f"{r[1]} ({r[2]})")
                for r in gramatas
            ]

            cursor.execute(
                """
                SELECT lasitaji_id, vards, uzvards, klase
                FROM lasitaji
                ORDER BY uzvards, vards
                """
            )
            lasitaji = cursor.fetchall()
            lasitaju_izvele.options = [
                ft.dropdown.Option(key=str(r[0]), text=f"{r[1]} {r[2]} ({r[3]})")
                for r in lasitaji
            ]

            #ja iepriekš bija izvēle, bet vairs nav options sarakstā
            if gramatu_izvele.value not in [o.key for o in gramatu_izvele.options]:
                gramatu_izvele.value = None
            if lasitaju_izvele.value not in [o.key for o in lasitaju_izvele.options]:
                lasitaju_izvele.value = None

        except Exception as e:
            statuss.value = f"Kļūda ielādējot dropdownus: {e}"

    #pievienot grāmatu
    gramata_nosaukums = ft.TextField(label="Nosaukums")
    gramata_autors = ft.TextField(label="Autors")
    gramata_gads = ft.TextField(label="Gads")
    gramata_zanrs = ft.TextField(label="Žanrs")

    def saglabat_gramatu(_):
        nosaukums = (gramata_nosaukums.value or "").strip()
        autors = (gramata_autors.value or "").strip()
        gads_txt = (gramata_gads.value or "").strip()
        zanrs = (gramata_zanrs.value or "").strip()

        if "" in [nosaukums, autors, gads_txt, zanrs]:
            statuss.value = "Kļūda: aizpildi visus grāmatas laukus!"
            page.update()
            return

        if not gads_txt.isdigit():
            statuss.value = "Kļūda: gads jābūt skaitlim!"
            page.update()
            return

        try:
            cursor.execute(
                """
                INSERT INTO gramatas (nosaukums, autors, gads, zanrs)
                VALUES (?, ?, ?, ?)
                """,
                (nosaukums, autors, int(gads_txt), zanrs),
            )
            savienojums.commit()
            
            statuss.value = "OK: grāmata pievienota!"
            gramata_nosaukums.value = ""
            gramata_autors.value = ""
            gramata_gads.value = ""
            gramata_zanrs.value = ""

            ieladet_dropdownus()
            page.update()
        except Exception as e:
            statuss.value = f"Kļūda saglabājot grāmatu: {e}"
            page.update()

    poga_saglabat_gramatu = ft.ElevatedButton(
        "Saglabāt grāmatu", on_click=saglabat_gramatu
    )

    #Pievienot lasītāju
    lasitajs_vards = ft.TextField(label="Vārds")
    lasitajs_uzvards = ft.TextField(label="Uzvārds")
    lasitajs_klase = ft.TextField(label="Klase")

    def saglabat_lasitaju(_):
        vards = lasitajs_vards.value or "".strip()
        uzvards = lasitajs_uzvards.value or "".strip()
        klase = lasitajs_klase.value or "".strip()

        if "" in [vards, uzvards, klase]:
            statuss.value = "Kļūda: aizpildi visus laukus!"
            page.update()
            return

        try:
            cursor.execute(
                """
                INSERT INTO lasitaji (vards, uzvards, klase)
                VALUES (?, ?, ?)
                """,
                (vards, uzvards, klase),
            )
            savienojums.commit()

            statuss.value = "Lasītājs pievienots!"
            lasitajs_vards.value = ""
            lasitajs_uzvards.value = ""
            lasitajs_klase.value = ""

            ieladet_dropdownus()
            page.update()
        except Exception as e:
            statuss.value = f"Kļūda saglabājot lasītāju: {e}"
            page.update()

    poga_saglabat_lasitaju = ft.ElevatedButton(
        "Saglabāt lasītāju", on_click=saglabat_lasitaju
    )

    #reģistrēt izņemtu grāmatu
    iznemsanas_datums = ft.TextField(label="Datums (YYYY-MM-DD)")
    atdots_checkbox = ft.Checkbox(label="Atdots")

    def saglabat_iznemumu(_):
        izveleta_gramata_id = gramatu_izvele.value
        izvelets_lasitajs_id = lasitaju_izvele.value
        datums = (iznemsanas_datums.value or "").strip()

        if not izveleta_gramata_id or not izvelets_lasitajs_id or datums == "":
            statuss.value = "Kļūda: izvēlies grāmatu, lasītāju un ievadi datumu!"
            page.update()
            return

        atdots = 1 if atdots_checkbox.value else 0

        try:
            cursor.execute(
                """
                INSERT INTO iznemtas_gramatas (gramatas_id, lasitaji_id, datums, atdots)
                VALUES (?, ?, ?, ?)
                """,
                (int(izveleta_gramata_id), int(izvelets_lasitajs_id), datums, atdots),
            )
            savienojums.commit()

            statuss.value = "OK: izņemšana reģistrēta!"
            iznemsanas_datums.value = ""
            atdots_checkbox.value = False
            page.update()
        except Exception as ex:
            statuss.value = f"Kļūda reģistrējot izņemšanu: {ex}"
            page.update()

    poga_saglabat_iznemumu = ft.ElevatedButton("Saglabāt", on_click=saglabat_iznemumu)
#3 pogas un 3 vaicājumi ar rezultātirm dialoglogā
    def izpildit_un_paradit(virsraksts,sql,kolonnas):
        try:
            cursor.execute(sql)
            rindas=cursor.fetchall()
            paradit_tabulu(virsraksts,kolonnas, rindas)
        except Exception as e:
            statuss.value=f"Kļūda vaicājumā: {e}"
            page.update()

    def vaicajums1(_): #atgriež visas grāmatas
        izpildit_un_paradit(
            "Visas grāmatas no datubāzes",
            "SELECT nosaukums, autors, gads, zanrs FROM gramatas ORDER BY nosaukums",
            ["Nosaukums","Autors","Gads","Žanrs"]
        )

    def vaicajums2(_): #atrast neatdotās grāmatas
        izpildit_un_paradit(
            "Neatdotās grāmatas no datubāzes",
            """
            SELECT gramatas.nosaukums, gramatas.autors,
            lasitaji.vards ||' '||lasitaji.uzvards,
            iznemtas_gramatas.datums
            FROM iznemtas_gramatas
            JOIN gramatas ON gramatas.gramatas_id=iznemtas_gramatas.gramatas_id
            JOIN lasitaji ON lasitaji.lasitaji_id = iznemtas_gramatas.lasitaji_id
            WHERE iznemtas_gramatas.atdots=0
            ORDER BY iznemtas_gramatas.datums DESC
            """,
            ["Grāmata","Autors","Lasītājs","Datums"]
        )

    poga_v1=ft.OutlinedButton("Visas grāmatas",on_click=vaicajums1)
    poga_v2=ft.OutlinedButton("Neatdotās grāmatas",on_click=vaicajums2)

    #ielādē dropdownus un uzzīmē
    ieladet_dropdownus()

    page.add(
        ft.Text("A) Pievienot grāmatu"),
        gramata_nosaukums,
        gramata_autors,
        gramata_gads,
        gramata_zanrs,
        poga_saglabat_gramatu,
        ft.Divider(),
        
        ft.Text("B) Pievienot lasītāju"),
        lasitajs_vards,
        lasitajs_uzvards,
        lasitajs_klase,
        poga_saglabat_lasitaju,
        ft.Divider(),
        
        ft.Text("C) Reģistrēt izņemtu grāmatu"),
        gramatu_izvele,
        lasitaju_izvele,
        iznemsanas_datums,
        atdots_checkbox,
        poga_saglabat_iznemumu,
        ft.Divider(),

        ft.Text("D) Vaicājumi"),
        ft.Row([poga_v1,poga_v2],wrap=True),
        ft.Divider(),
        statuss,
    )

    page.update()

ft.app(target=main)
