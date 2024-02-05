#vienkārša funkcija ar lietotāja datu ievadi un nosacījumiem
def parbaudit_skaitli(skaitlis):
    if skaitlis>0:
        print('Skaitlis ir pozitīvs')
    elif skaitlis<0:
        print('Skaitlis ir negatīvs')
    else:
        print('Skaitlis ir 0')

liet_skaitlis= float(input('Ievadiet skaitli: '))
parbaudit_skaitli(liet_skaitlis)