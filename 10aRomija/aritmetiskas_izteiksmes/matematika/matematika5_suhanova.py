import math
vards_uzvards = (input('Programmu izstrādāja: ')) #lietotājs ievada savu vārdu uzvārdu
print('Laukuma aprēķins ģeometriskām figūrām')
print('\t****')
a_mala = (input('Ievadiet malas A garumu:')) #ievada a malu
print(a_mala)
print('Malas A garums: ', float(a_mala)) #izdrukā ar decimālciparu
print('\t****')
b_mala = (input('Ievadiet malas A garumu:')) #ievada b malu
print(b_mala)
print('Malas B garums: ', float(b_mala)) #izdrukā ar decimālciparu
print('\t****')
augstums = (input('Ievadiet augstumu: ')) #lietotājs ievada augstumu
print('Augstums: ', float(augstums)) #izdrukā augstumu ar decimālciparu
reizinajums = a_mala * augstums  #a*h
laukums = reizinajums/2  #(a*h)/2
print('Laukums trijstūrim: ' "%.1f"%laukums) #noformē laukumu
a_plus_b = a_mala + b_mala   #a+b
dalijums = a_plus_b/2  #(a+b)/2
laukums2 = dalijums * augstums
print('Laukums trapecei: ' "%.1f"%laukums2)

