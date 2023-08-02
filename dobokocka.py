from random import randint

"""
Kockavető v0.1
--------------
Normál dobókocka (1-6), illetve színes dobókocka (fehér, sárga, narancs, piros, zöld, kék) van beállítva

Fejlesztési lehetőségek:
- további "kockák" beépítése
- "kockák" kiválasztásának lehetősége
- körök számolása
- grafikus felület
"""

kocka = ["1", "2", "3", "4", "5", "6"]
szinek = ["fehér", "sárga", "narancs", "piros", "zöld", "kék"]
jatekosok = []
i = 1

print("Szia!\n"
      "Ez egy kockavető játék, 'pöttyös' (1-6), illetve színes dobókocka szimulálására.\n"
      "Add meg a játékosok számát, majd a nevét, és kezdődhet is a játék.\n"
      "A következő játékos 'dobásához' csak üss egy entert. A játék befejezéséhet írj be egy 'v' betűt.\n")
jatekosok_szama = int(input("Hányan szeretnétek játszani? "))

while i <= jatekosok_szama:
    print(str(i) + ". játékos neve: ")
    nev = input()
    jatekosok.append(nev)
    i += 1

list_elem = jatekosok_szama

input("\nKezdhetjük?\n")

while list_elem <= len(jatekosok):
    if list_elem >= jatekosok_szama:
        list_elem = 0
    else:
        dobas = kocka[randint(0, 5)], szinek[randint(0, 5)]
        print(str(jatekosok[list_elem]) + " dobása: " + dobas[0] + ", " + dobas[1] + "\n")
        list_elem += 1
        kov = input("Jöhet a következő játékos? ")
        if kov == "v":
            exit()
        else:
            continue
