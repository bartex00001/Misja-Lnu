from wieki_krasnali import wieki_krasnali
from wiek import wiek
import datetime
import random


def najstarszy(krasnale):
    najstarsza_data = datetime.datetime.now()
    najstarszy_imie = ""

    for i in krasnale:
        nowa_data = datetime.datetime.strptime(i['date'], r"%d.%m.%Y")
        nowy_imie = i['name']
        if nowa_data < najstarsza_data:
            najstarsza_data = nowa_data
            najstarszy_imie = nowy_imie
        elif nowa_data == najstarsza_data:
            if nowy_imie < najstarszy_imie:
                najstarszy_imie = nowy_imie
    
    return najstarszy_imie

def test():
    ilosc = random.randint(5, 100)
    krasnale = random.choices(wieki_krasnali, k=ilosc)

    correct = najstarszy(krasnale)

    try:
        answer = wiek(krasnale)

        if answer == correct:
            komunikat = "Hmm... chyba masz rację!"
            return True
        else:
            komunikat = "Jesteś pewien? Jakoś inaczej to zapamiętałem..."
            return False

    except:
        komunikat = "Coś poszło nie tak..."
        return False
