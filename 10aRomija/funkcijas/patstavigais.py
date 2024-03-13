svars = float(input('Ievadi savu svaru: '))
augums = float(input('Ievadi savu augumu: '))

def masa():
    print(f'ĶMI: {svars/augums*augums}')

if svars/augums*augums<18.5:
    print("Nepietiekama ķermeņa masa")

elif 18.5<=svars/augums*augums<=24.99:
    print("Normāla ķermeņa masa")

elif 25<=svars/augums*augums<=29.99:
    print('Lieka ķermeņa masa')

else:
    print('Aptaukošanās')

