from sys import warnoptions
from reszta import reszta
import random
from math import ceil


KOSZT_MAGNESU = 5.40
KOSZT_DLUGOPISU = 3.49
KOSZT_POCZTOWKI = 2.99
KOSZT_FIGURKI = 10.35


def test():
    ilosc_magnesow = random.randint(0, 5)
    ilosc_dlugopisow = random.randint(0, 8)
    ilosc_pocztowek = random.randint(0, 10)
    ilosc_figurek = random.randint(0, 3)

    koszt = ilosc_magnesow * KOSZT_MAGNESU + ilosc_dlugopisow * KOSZT_DLUGOPISU + ilosc_pocztowek * KOSZT_POCZTOWKI + ilosc_figurek * KOSZT_FIGURKI

    zaplacona_kwota = koszt + random.randint(0, 15)

    if random.choice((0,2)) == 0:
        zaplacona_kwota = ceil(zaplacona_kwota)


    try:
        
        wartosc = reszta(zaplacona_kwota, ilosc_magnesow, ilosc_dlugopisow, ilosc_pocztowek, ilosc_figurek)

        komunikat = f"reszta( {zaplacona_kwota}, {ilosc_magnesow}, {ilosc_pocztowek}, {ilosc_figurek}) = {wartosc}: "
        print(round(zaplacona_kwota-koszt, 2))


        if wartosc == round(zaplacona_kwota - koszt, 2):
            komunikat += "Wszystko dobrze!"
            return True
        else:
            komunikat += "Chyba coś źle policzyłeś..."
            return False
    except Exception:
        komunikat = "Coś poszło nie tak..."
        return False
