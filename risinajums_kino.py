import sqlite3
import flet as ft

def main(page: ft.Page):
    page.title = "Kino seansi"
    page.window_width = 900
    page.window_height = 650

    savienojums = sqlite3.connect("skolas_kino_db.db")
    cursor = savienojums.cursor()

    virsraksts = ft.Text("Kino seansu vaicājumi",size=22,weight=ft.FontWeight.BOLD)
    #dropdown izvēlne - filmu nosaukumi no db
    filmas_dropdown = ft.Dropdown(
        label = "Izvēlies filmu: ",#txt, ko redz lietotājs
        width=350,
        options = [] #iespējamās izvēles, ko vēlāk nolasīt no tabulas filma
    )
    statusa_teksts=ft.Text("",color="red") #teksts kļūdai

    #tabula rezultātu attēlošanai
    #kolonnas: filmas nosaukums|zāle|datums|laiks|cena
    #rindas tiks mainītas pēc katra vaicājuma
    rezultatu_tabula=ft.DataTable(
        columns=[
        ft.DataColumn(ft.Text("Filma")),
        ft.DataColumn(ft.Text("Zāle")),
        ft.DataColumn(ft.Text("Datums")),
        ft.DataColumn(ft.Text("Laiks")),
        ft.DataColumn(ft.Text("Cena")),
        ],
    rows=[]
    )

    def paradit_tabulu(rezultati): #šī funkcija saņem SQL rez(sarakstu ar rindām) un ieliks tabulā
        rezultatu_tabula.rows=[] #sākumā notīra vecās rindas
        #ja nekas nav atrasts, parādīt paziņojumu (tabulu atstāj tukšu)
        if not rezultati:
            statusa_teksts.value="Nav atbilstošu seansu."
            page.update()
            return
        #ja ir rez, tad noņem paziņojumu
        statusa_teksts.value=""

        #izveidot DataRow katrai rindai
        for rinda in rezultati:
            cells = [
                ft.DataCell(ft.Text(str(rinda[0]))),
                ft.DataCell(ft.Text(str(rinda[1]))),
                ft.DataCell(ft.Text(str(rinda[2]))),
                ft.DataCell(ft.Text(str(rinda[3]))),
                ft.DataCell(ft.Text(str(rinda[4]))),
            ]
            rezultatu_tabula.rows.append(ft.DataRow(cells= cells))
        page.update()

        #filmu nosaukumi dropdown izvēlē
        #atlasīt filmas sakartotas pēc nosaukums
    cursor.execute("SELECT nosaukums FROM filmas ORDER BY nosaukums")
    filmas=cursor.fetchall()
    #pārvērst rez par dd opcijām
    options = []
    for f in filmas:
        options.append(ft.dropdown.Option(f[0]))
    filmas_dropdown.options = options

    #vaicājums 2 - filtrēt seansus pēc filmas nosaukuma
    def filtret_seansus_pec_filmas(_):
        izveleta_filma = filmas_dropdown.value
        #ja lietotājs nav izvēlējies filmu, parāda paziņojumu
        if not izveleta_filma:
            statusa_teksts.value="Izvēlies filmu, tad spied filtret"
            rezultatu_tabula.rows=[]
            page.update()
            return
        
        sql="""
        SELECT 
            filmas.nosaukums,
            zales.nosaukums,
            seansi.datums,
            seansi.sakuma_laiks,
            seansi.cena
        FROM seansi
        JOIN filmas ON seansi.filma_id = filmas.filma_id
        JOIN zales ON seansi.zale_id = zales.zale_id
        WHERE filmas.nosaukums = ?
        """
        cursor.execute(sql,(izveleta_filma,))
        rezultati = cursor.fetchall()
        paradit_tabulu(rezultati)

        #poga rezultatiem
    poga_filtret = ft.ElevatedButton("Filtrēt seansus",on_click=filtret_seansus_pec_filmas)




    page.add(virsraksts,
            ft.Row([filmas_dropdown,poga_filtret],wrap = True),
            statusa_teksts,
            ft.Text("Rezultāti: ",size=16,weight=ft.FontWeight.BOLD),
            ft.Container(rezultatu_tabula,padding=10),
        )
ft.app(target=main)