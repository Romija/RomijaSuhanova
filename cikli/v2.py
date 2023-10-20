'''atbilde = 'j'
while atbilde == 'j':
    print('Nekusties!')
    atbilde = input('vai brismonis ir draudzīgs? (j/n)')
print('Bēdz prom!')'''

#pārbaudīt vai lietotājs prot reizināt līdz 7
#programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jaut
reiz = 7
for i in range(1,13): #cikla mainīgais no 1-12
    print('Cik ir',i,'*',reiz,'?')
    minejums = input() #nevar int jo tekstu nesalīdzinās
    if minejums == 'stop':
        break #pārtrauc programmu, bet ieskaitē to nerakstīt,jo nav labs stils
    if minejums == 'izlaist':
        print('Tiek izlaists ')
        continue #izlaiž 1 jaut bet turpina tālāk
    atb = i * reiz
    if int(minejums) ==atb:
        print('Pareizi')
    else:
        print('Nē, tas ir',atb)
        #ja ir nepareizi, ta atgriežas pie jaut
        #reizinātāju ievada lietotājs