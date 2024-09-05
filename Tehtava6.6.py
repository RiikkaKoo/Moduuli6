import math

def neliometri_hinta(halkaisija,eurot):
    pinta_ala = ((halkaisija/2)**2)*math.pi
    pinta_ala_m = pinta_ala/100
    hinta = eurot/pinta_ala_m
    return hinta

print("Lasketaan kahden pizzan yksikköhinta per neliömetri.")
print()
eka_halkaisija = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
eka_eurot = float(input("Anna ensimmäisen pizzan hinta euroina: "))
print()
toka_halkaisija = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
toka_eurot = float(input("Anna toisen pizzan hinta euroina: "))
print()

eka_neliometri_hinta = neliometri_hinta(eka_halkaisija, eka_eurot)
toka_neliometri_hinta = neliometri_hinta(toka_halkaisija, toka_eurot)

if eka_neliometri_hinta > toka_neliometri_hinta:
    print(f"Toinen pizza on parempaa vastinetta rahalle. Sen yksikköhinta on {toka_neliometri_hinta:.2f} euroa/neliömetri, \n"
          f"kun taas ensimmäisen pizzan yksikköhinta on {eka_neliometri_hinta:.2f} euroa/neliömetri.")
else:
    print(f"Ensimmäinen pizza on parempaa vastinetta rahalle. Sen yksikköhinta on {eka_neliometri_hinta:.2f} euroa/neliömetri, \n"
          f"kun taas toisen pizzan yksikköhinta on {toka_neliometri_hinta:.2f} euroa/neliömetri.")