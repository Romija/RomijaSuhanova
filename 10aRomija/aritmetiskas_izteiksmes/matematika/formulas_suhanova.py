import math
import random
radiuss = float(input('Ievadiet riņķa līnijas rādiusu: ')) #radiuss ir ievadītais riņķa līnijas rādiuss
print(int(radiuss))
print(radiuss)
PI = 3.14159
rl = 2*PI*radiuss # rl ir riņķa līnijas formula
print('Riņķa līnijas garums: ' "%.2f"%rl) #mainīgais rl noformēts ar 2 cip aiz komatiem
laukums = PI * math.pow(radiuss,2) #laukums ir mainīgais ar laukuma vērtību
print('Riņķa līnijas laukums: ' "%.2f"%laukums) #izdrukā riņķa līnijas laukumu un noformē aiz 2 cipariem aiz komata

k1 = int(input('Ievadiet taisnleņķa trijstūra pirmās katetes garumu: ')) #ievada pirmo kateti
k2 = int(input('Ievadiet taisnleņķa trijstūra otrās katetes garumu: ')) #ievada otro kateti

h = math.pow(k1,2) + math.pow(k2,2) #h ir katešu summa
h2 = math.sqrt(h) #izvelk kvadrātsakni
print('Taisnleņķa hipotenūzas garums: ' "%.2f"%h2) #noformē aiz 2 cipariem aiz komata

cipars = random.random() #0 - 1
print(cipars)
