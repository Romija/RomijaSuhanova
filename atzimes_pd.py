def sveicieni():
    print("Sveicieni! :)")

import datetime

def datuma_ievade():
    while True:
        datums = input("Lūdzu ievadiet datumu formātā YYYY-MM-DD: ")
        try:
            # Mēģinām pārvērst ievadīto virkni par datetime objektu
            date = datetime.datetime.strptime(datums, "%Y-%m-%d").date()
            # Pārbaudām, vai ievadītais datums nav nākotnē
            if date > datetime.date.today():
                print("Nevar ievadīt datumu no nākotnes. Lūdzu ievadiet datumu līdz šodienai vai agrāk.")
                continue
            else:
                return date
        except ValueError:
            # Ja datums nav pareizi formatēts
            print("Nepareizs formāts. Lūdzu ievadiet datumu pareizajā formātā.")

def skolena_info():
    global klase, tema
    datuma_ievade()
    klase = input("Ievadi klasi: ")
    tema = input("Ievadi tēmu: ")

def skaits_sk():
    global skaits
    while True:
        try:
            skaits = int(input("Ievado skolēnu skaitu: "))
            if skaits <= 0 or skaits>18:
                print('Max ir 18')
                continue
            else:
                return skaits
        except ValueError:
            print('Nepareiza ievade')

def skolenu_vardi():
    vardi = []
    for i in range(skaits):
        vards = input(f'Lūdzu ievadiet {i+1}. skolēna vārdu: ')
        vardi.append(vards)
    return vardi

def ievadit_atzimi():
    while True:
        try:
            atzime = int(input("Lūdzu, ievadiet atzīmi no 1 līdz 10: "))
            if 1 <= atzime <= 10:
                return atzime
            else:
                print("Kļūda: Ievadītais skaitlis nav no 1 līdz 10. Lūdzu, mēģiniet vēlreiz.")
        except ValueError:
            print("Kļūda: Ievadītajam vērtībai jābūt skaitlim. Lūdzu, mēģiniet vēlreiz.")

def izveidot_vai_papildinat_failu():
    global klase, tema
    skolena_info()
    skaits_sk()
    vardi = skolenu_vardi()

    filename = f"{klase}_{tema}.txt"

    try:
        with open(filename, 'a') as f:
            for skolens in vardi:
                f.write(skolens + '\n')
        print(f"Failā '{filename}' veiksmīgi saglabāti skolēnu vārdi.")
    except Exception as e:
        print(f"Kļūda, nevarēja saglabāt failā: {e}")

while True:
    izveidot_vai_papildinat_failu()
    atbilde = input("Vai vēlaties turpināt? (jā/nē): ")
    if atbilde.lower() != 'jā':
        break
