import flet as ft #importē flet bibliotēku
#sākas ar funkciju, kurai padod page objektu

def main(page: ft.Page):
    page.title="5. janvāris"
    teksts=ft.Text("Sveika, pasaule!")
    poga=ft.ElevatedButton("Nospied mani")
    page.add(teksts, poga)

ft.app(target=main) #startē logu, izsauc main(page)

