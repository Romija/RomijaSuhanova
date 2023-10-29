suna_vecums = int(input('Ievadi suņa gadus: '))
if suna_vecums == 1 or suna_vecums == 2: #likt ar mainīgo arī otro, jo citādāk nestrādā 
    suna_vecums1 = suna_vecums*10.5
    print('Sunim ir',suna_vecums1,'gadu')
elif suna_vecums>=3:
    suna_vecums2 = suna_vecums*4 +21
    print('Sunim ir ',suna_vecums2,'gadu')
else:
    print('Ievadiet korektus datus')