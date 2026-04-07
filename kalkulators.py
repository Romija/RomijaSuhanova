#var nelikt konstuktoru, jo klase 
#tikai definē metodes, kas veic aprēķinus ar padotajiem parametriem a un b.

#klases definēšana
class Kalkulators:
  def saskaiti(self, a, b):
    return a + b

  def atnem(self, a, b):
    return a - b

  def reizini(self, a, b):
    return a * b

  def dali(self, a, b):
    if b == 0:
      return "Dalīšana ar nulli nav atļauta!"
    else:
      return a / b

#objekta izveidošana
kalkulators = Kalkulators()

print("Kalkulators")
print("1. Saskaitīšana")
print("2. Atņemšana")
print("3. Reizināšana")
print("4. Dalīšana")

while True:
  izvele = input("Izvēlies darbību (1/2/3/4): ")

  if izvele not in ('1', '2', '3', '4'):
    print("Nepareiza darbības izvēle. Lūdzu, mēģini vēlreiz!")
    continue

  a = float(input("Ievadi pirmo skaitli: "))
  b = float(input("Ievadi otro skaitli: "))

  if izvele == '1':
    rezultats = kalkulators.saskaiti(a, b)
    print(f"Saskaitīšanas rezultāts: {rezultats}")
  elif izvele == '2':
    rezultats = kalkulators.atnem(a, b)
    print(f"Atņemšanas rezultāts: {rezultats}")
  elif izvele == '3':
    rezultats = kalkulators.reizini(a, b)
    print(f"Reizināšanas rezultāts: {rezultats}")
  elif izvele == '4':
    rezultats = kalkulators.dali(a, b)
    print(f"Dalīšanas rezultāts: {rezultats}")

  turpinat = input("Vēlreiz? (Jā/Nē): ")
  if turpinat.lower() != "jā":
    break


#tas būs jēgpilns tikai tad, ja  grib saglabāt skaitļus klasē, nevis katrā metodē padot kā parametrus
#nozīmē, ka: a un b tiek pievienoti objektam kā atribūti
#tie dzīvo objektā kalkulators, nevis tikai funkcijas ietvaros

class Kalkulators:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def saskaiti(self):
        return self.a + self.b

    def atnem(self):
        return self.a - self.b

    def reizini(self):
        return self.a * self.b

    def dali(self):
        if self.b == 0:
            return "Dalīšana ar nulli nav atļauta!"
        return self.a / self.b


print("Kalkulators")
print("1. Saskaitīšana")
print("2. Atņemšana")
print("3. Reizināšana")
print("4. Dalīšana")

while True:
    izvele = input("Izvēlies darbību (1/2/3/4): ")

    if izvele not in ('1', '2', '3', '4'):
        print("Nepareiza darbības izvēle!")
        continue

    a = float(input("Ievadi pirmo skaitli: "))
    b = float(input("Ievadi otro skaitli: "))

    kalkulators = Kalkulators(a, b)  # onstruktors tiek izmantots šeit

    if izvele == '1':
        print(kalkulators.saskaiti())
    elif izvele == '2':
        print(kalkulators.atnem())
    elif izvele == '3':
        print(kalkulators.reizini())
    elif izvele == '4':
        print(kalkulators.dali())

    if input("Vēlreiz? (Jā/Nē): ").lower() != "jā":
        break