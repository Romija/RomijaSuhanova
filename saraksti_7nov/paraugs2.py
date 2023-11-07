krasas = ['rozā','dzeltens','balts','zils']
jauns = []
for i in krasas:
    burti = 0
    for burts in i:
        burti +=1
    pagaidu_saraksts = [i,burti]
    jauns.append(pagaidu_saraksts)
print(jauns)

for krasa in krasas:
    print(krasa,len(krasa))