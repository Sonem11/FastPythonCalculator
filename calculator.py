# Ovo je naš prvi Python projekat: jednostavan kalkulator

# Funkcija input() služi da korisnik unese vrednost sa tastature.
# Funkcija float() pretvara taj unos u broj (decimalni).
broj1 = float(input("Unesi prvi broj: "))

# Isto radimo i za drugi broj.
broj2 = float(input("Unesi drugi broj: "))

# Sada pitamo korisnika koju operaciju želi da uradi.
# Koristimo string jer unos može biti +, -, *, /
operacija = input("Izaberi operaciju (+, -, *, /): ")

# Sada koristimo if-elif-else da odlučimo šta da uradimo na osnovu operacije.
if operacija == "+":
    print("Rezultat je:", broj1 + broj2)
elif operacija == "-":
    print("Rezultat je:", broj1 - broj2)
elif operacija == "*":
    print("Rezultat je:", broj1 * broj2)
elif operacija == "/":
    # Dodajemo proveru da ne delimo sa nulom.
    if broj2 != 0:
        print("Rezultat je:", broj1 / broj2)
    else:
        print("Greška: deljenje sa nulom nije dozvoljeno.")
else:
    print("Nepoznata operacija.")
