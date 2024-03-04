'''ļaut ievadīt tekstu, ierakstīt to failā
teksta_fails.txt. ievadīt skaitli, papildināt
ar šo skaitli, katru rinndu sākot ar 
papildus rindas nr'''

def ierakstit_faila():
    teksts=input('Ievadi teikumu: ')

    with open('teksta_fails.txt','w',encoding='utf8') as file:
        file.write(teksts)

def papildus_skaitlis():
    skaitlis=int(input('Ievadiet veselu skaitli: '))

    with open('teksta_fails.txt','a',encoding='utf8') as file: # a updato/papildina
        for i in range(skaitlis):
            file.write(f'\nPapildus rindas nr. {i+1}')



ierakstit_faila()
papildus_skaitlis()