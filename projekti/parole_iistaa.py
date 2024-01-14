print('Ievadiet stop ievadē, ja vēlaties apstādināt programmu')
pareizs_lietotajvards = 'skolens' #pareizais lietotājvārds
pareiza_parole = '12345' #pareizā parole
meginajumi = 0

while meginajumi < 5:
    lietotajvards = input("\nIevadiet lietotājvārdu: ")
    if lietotajvards == 'stop':
        exit()
    parole = input("Ievadiet paroli: ")
    paroles_garums = len(parole) #paroles garums
    if parole == 'stop':
        exit()
    
    if lietotajvards == pareizs_lietotajvards and parole == pareiza_parole:
        print('Pieslēgšanās veiksmīga!') #turpinās 2.uzdevums
        skaitlis1 = input('Ievadi pirmo veselo skaitli: ')
        if skaitlis1 == 'stop':
            exit()
        skaitlis2 = input('Ievadi otro veselo skaitli: ')
        if skaitlis2 == 'stop':
            exit()

        if int(skaitlis1)<0 or int(skaitlis2)<0: #nevar būt negatīvi
            print('Nedrīkst būt negatīvs skaitlis!')
        elif int(skaitlis1)>int(skaitlis2): #pirmajam jābūt mazākam
            print('0')
        else:
            while int(skaitlis1)<int(skaitlis2): 
                summa = int(skaitlis1) + int(skaitlis2)
                for i in range (int(skaitlis1)+1,int(skaitlis2)):
                    summa+=i
                print('Veselu secīgi pieaugušo skaitļu no',skaitlis1,'līdz',skaitlis2, 'summa ir: ',summa)
                exit()
    else:
        meginajumi += 1
        atlikusie_meginajumi = 5 - meginajumi
        print(f"Atlikušie mēģinājumi: {atlikusie_meginajumi}")
        if paroles_garums !=5:
            print('Parolē ir jābūt 5 rakstzīmēm!')
            
if meginajumi == 5:
    exit()


    #komentāri jāsaliek
    #pārbaudīt negatīvos
    #par rakstzīmēm
    #pārbaudīt p un n pie inputiem
