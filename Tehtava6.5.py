
eka_lista = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,43,99,73,46, 88, 456,55,99]

def listan_muokkaus(lista):
    parilliset = []
    for i in lista:
        jakojaannos = i % 2
        if jakojaannos == 0:
            parilliset.append(i)
    return parilliset

print(eka_lista)
uusi_lista = listan_muokkaus(eka_lista)
print(uusi_lista)