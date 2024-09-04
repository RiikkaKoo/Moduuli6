def yhteenlasku(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    return summa

kokonaisluvut = []
luku = input("Anna kokonaisluku: ")
while luku != "":
    kokonaisluku = int(luku)
    kokonaisluvut.append(kokonaisluku)
    luku = input("Anna kokonaisluku: ")

laskettu = yhteenlasku(kokonaisluvut)
print(laskettu)