import random

maksimi = False

def nopanheitto(arvo):
    b = arvo
    heitto = int(random.randint(1,b))
    return heitto

tahkot = int(input("Anna nopan tahkojen määrä: "))
print("Heitetään noppaa, kunnes saadaan maksimisilmäluku!")

while not maksimi:
    luku = nopanheitto(tahkot)
    print(luku)
    if luku == tahkot:
        print(F"Maksimisilmäluku {luku}!")
        maksimi = True