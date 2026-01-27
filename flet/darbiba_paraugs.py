import flet as ft #importē flet bibliotēku
#sākas ar funkciju, kurai padod page objektu

def main(page: ft.Page):
    page.title="Paraugs"

#2. daļa - objekts
    teksts = ft.Text("Gaida darbību")
#3.daļa - darbība
    def poga_nospiesta(_):
        teksts.value = "Poga nospiesta!"
        page.update()
#4. daļa - sasaistīšana
    poga = ft.ElevatedButton("Nospied!",on_click=poga_nospiesta)

#5. izkārtojums
    page. add(teksts, poga)

ft.app(target=main)
