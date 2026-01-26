import flet as ft
def main(page:ft.Page):

    page.title = "Dažādi piemēri"
    #lielais virsraksts
    virsraksts=ft.Text(
        value="5. janvāra stunda",
        size = 27,
        weight = ft.FontWeight.BOLD,
        color = "blue"
    )

    #ievades lauki vārdam un uzvārdam
    vards = ft.TextField(
        label = "Ievadi vārdu: ",
        width=200 #platums px
    )

    uzvards = ft.TextField(
        label = "Ievadi uzvārdu: ",
        width=200 #platums px
    )

    #rezultāta teksts(mainīsies, nospiežot pogu)
    rezultats=ft.Text(value = "Te būs rezultāts", size = 20, color="green")


    #dialoglogs(alert logs)
    dialogs = ft.AlertDialog(
        title = ft.Text("Papildu logs"),
        content=ft.Text("šis ir teksts"),
    actions = [
    #pogas, kas būs mazajā logā
    ft.TextButton("Aizvērt",on_click=lambda e:page.close(dialogs)) #aizvērs logu
    ]
)
    #funkcija, kas parādīs sveicienu(nedrīkst atstāt tukšu lauku)
    def paradit_sveicienu(_):
        if vards.value.strip()=="" or uzvards.value.strip()=="":
            rezultats.value = "Lūdzu, aizpildiet abus laukus"
            rezultats.color="green"
        else:
            rezultats.value=f"Sveiks, {vards.value} {uzvards.value}"
            rezultats.color="green"
        #atjaunot lapu, lai redzētu izmaiņas
        page.update()

#poga, kas parādīs sveicienu(izsauks funkciju)
    poga_sveiciens=ft.ElevatedButton(
        "Parādīt sveicienu",
        on_click=paradit_sveicienu
    )

#funkcija, kas atver dialoga logu
    def atvert_logu(_):
        page.open(dialogs)
        #sasaista funkciju
    poga_logs = ft.OutlinedButton(
        "Atvērt otro logu", on_click=atvert_logu
    )


    page.add(virsraksts,
            vards,
            uzvards,
            poga_sveiciens,
            poga_logs,
            rezultats)

ft.app(target=main)