# Input keempat bilangan
bilangan1 = 60
bilangan2 = 20
bilangan3 = 100
bilangan4 = 40

# Bandingkan bilangan pertama dengan bilangan kedua
if bilangan1 > bilangan2:
    if bilangan1 > bilangan3:
        if bilangan1 > bilangan4:
            print("Bilangan pertama ({}) adalah nilai terbesar.".format(bilangan1))
        else:
            print("Bilangan keempat ({}) adalah nilai terbesar.".format(bilangan4))
    else:
        if bilangan3 > bilangan4:
            print("Bilangan ketiga ({}) adalah nilai terbesar.".format(bilangan3))
        else:
            print("Bilangan keempat ({}) adalah nilai terbesar.".format(bilangan4))
else:
    if bilangan2 > bilangan3:
        if bilangan2 > bilangan4:
            print("Bilangan kedua ({}) adalah nilai terbesar.".format(bilangan2))
        else:
            print("Bilangan keempat ({}) adalah nilai terbesar.".format(bilangan4))
    else:
        if bilangan3 > bilangan4:
            print("Bilangan ketiga ({}) adalah nilai terbesar.".format(bilangan3))
        else:
            print("Bilangan keempat ({}) adalah nilai terbesar.".format(bilangan4))
