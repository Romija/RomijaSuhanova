vecums = int(input('Ievadiet suņa vecumu: '))
if vecums == 1 or 2:
    suna_vecums1 = vecums*10.5
    print('Suns ir',suna_vecums1,'vecs')
elif vecums >=3:
    suna_vecums2 = 21+vecums*4
    print('Suns ir',suna_vecums2,'vecs')
else:
    print('Lūgums ievadīt korektus datus')