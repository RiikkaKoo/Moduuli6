import random

kuusi = False
def nopanheitto():
    heitto = int(random.randint(1,6))
    return heitto

print("Heitetään noppaa, kunnes saadaan kuutonen!")
while kuusi == False:
    luku = nopanheitto()
    print(luku)
    if luku == 6:
        print("Kuutonen!")
        kuusi = True