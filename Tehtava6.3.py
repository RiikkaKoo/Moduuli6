def litroiksi(gallonat):
    gallonaa = float(gallonat)
    litraa = gallonaa * 3.785
    return litraa

bensiini = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina: "))
while bensiini >= 0:
    muunnos = litroiksi(bensiini)
    print(f"{bensiini:.3f} gallonaa on {muunnos:.3f} litraa.")
    print()
    bensiini = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonoina: "))
else:
    print("Negatiivinen gallonamäärä.")