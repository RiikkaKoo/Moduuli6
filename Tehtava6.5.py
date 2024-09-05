
#Toimii pienemmillä luvuilla, mutta osan isompien parittomien lukujen (tässä 43 ja 73 myös toinen 99) jakojäännöksestä (0.5) ei
# jostain syystä tunnisteta isommaksi kuin nolla, eli ne pääsevät lipsahtamaan uuteen listaan.
# Missä ongelma?

eka_lista = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,43,99,73,55,99]

def listan_muokkaus(lista):
    muokkaus = lista
    for i in muokkaus:
        jakojaannos = i % 2
        if jakojaannos != 00.000:
            muokkaus.remove(i)
    return muokkaus

print(eka_lista)
uusi_lista = listan_muokkaus(eka_lista)
print(uusi_lista)