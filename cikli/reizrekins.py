'''n = int(input("Ievadīt skaitli:"))

for i in range(1,11):
    print(n,'+',i,'=',n+i)
print('--------')'''
#atrast skaitļu 2 un 4 dalītājus
#uz ekrāna parādīt tos, kas dalās ar 2, un atsevišķi ar abiem
#range 50
#dc pieejami citi risinājumi
for i in range(51):
    if i%2==0 and i%4==0:
        print(i,'dalās gan ar 2, gan ar 4')
    elif i%2==0:
        print(i,'dalās tikai ar 2')
    else:
        print(i,'nedalās')