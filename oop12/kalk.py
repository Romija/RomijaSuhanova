class Kalkulators:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def saskaitit(self):
        print("Summa: ",int(a)+int(b))
    def atnemt(self):
        print("Starpība: ", int(a)-int(b))
    def reiz(self):
        print("Reizinājums: ",int(a)*int(b))
    def dalit(self):
        print("Dalījums: ",int(a)/int(b))

while True:
    while True:
        a = input("Ievadi skaitli a: ")
        if not a.isdigit():
            print("Jāievada skaitlis.")
            continue
        else:
            break
    while True:
        b = input("Ievadi skaitli b: ") #nulles pārbaude
        if not b.isdigit():
            print("Jāievada skaitlis.")
            continue
        else:
            break

    c = Kalkulators(a,b)

    while True:
        ievade = input("Ko vēlies darīt (+,-,*,/): ")
        
        if ievade == "+":
            c.saskaitit()
        elif ievade == "-":
            c.atnemt()
        elif ievade == "*":
            c.reiz()
        elif ievade == "/":
            c.dalit()
        else:
            print("Nederīga ievade.")
