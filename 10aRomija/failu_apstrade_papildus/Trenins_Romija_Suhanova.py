def sveiciens():
    print('-------\nLabs rīts! Ievadi "iziet", ja vēlies iziet jebkurā brīdī\n-------')

from datetime import datetime
import re #vajadzīgs, lai varētu noņemt atstarpes vēlāk

def iegut_datus(): 
    #funkcija, kas pieprasa datus un pārbauda, vai lietotājs vēlas iziet
    global eksperimenta_nosaukums, vards, laiks, vieta #atgriež vērtības
    eksperimenta_nosaukums = input("Ievadi eksperimenta nosaukumu: ")
    if eksperimenta_nosaukums == "iziet": #pārbauda, vai lietotājs nevēlas iziet
        print("Programmas beigas!")
        exit()
    vards = input("Ievadi skolēna vārdu: ")
    if vards == "iziet":
        print("Programmas beigas!")
        exit()
    laiks = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #aizpilda laiku automātiski
    vieta = input("Ievadi eksperimenta vietu: ")
    if vieta == "iziet":
        print("Programmas beigas!")
        exit()

def pareizs_vards():
    global vards_bez_atstarpem, vards_pareizais #atgriež vērtības
    vards_bez_atstarpem= re.sub(r'\s', '', vards) #noņem atstarpes ar iebūvēto funkciju
    vards_pareizais = vards_bez_atstarpem.capitalize() #pieliek lielo burtu


def saglabat_datus():
    #funkcija, kas ieraksta visu failā un saglabā
    with open('eksperimenta_dati.txt','a',encoding='utf8') as fails:
        fails.write(f'Vārds: {vards_pareizais}, eksperimenta nosaukums: {eksperimenta_nosaukums}, vieta: {vieta}, laiks: {laiks}\n')

def galvena():
    #funkcija, kas izsauc pārējās un tas iet pa ciklu līdz lietotājs vēlas iziet
    while True:
        sveiciens()
        iegut_datus()
        pareizs_vards()
        saglabat_datus()

galvena()
