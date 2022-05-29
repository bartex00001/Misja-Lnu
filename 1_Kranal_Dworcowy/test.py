from przywitanie import przywitanie
import random


# Wielka lista krasnalich imion DO ZROBIENIA
wszystkie_imiona = ["Ala", "Basia", "Cezary", "Dariusz", "Emperariusz", "Falkoniusz", "Gampeniusz", "Hapek", "Innocenty", "Janusz", "Kapgeminiusz", "Lola", "Łucja",
                    "Manna", "Nastazja", "Oliwandra", "Programiusz", "Quarka", "Roweracja", "Stanisława", "Teodora", "Uwertura", "Wojsław", "Xavery", "Yeeeti", "Zenon"]


def rozwiazanie(lista_imion):
    return ["Witaj " + i + "!" for i in lista_imion]

def test():
    lista_imion = random.choices(wszystkie_imiona, k=random.randint(1, 10))

    try:
        wartosc = przywitanie(lista_imion)
        oczekiwana = rozwiazanie(lista_imion)

        if wartosc == oczekiwana:
            komunikat = "Dzięki za pomoc! Wszystkie karteczki wyglądają bezbłędnie!\n" + str(wartosc)
            return True
        else:
            komunikat = "Coś nie do końca wyszło? Jesteś pewien że ten program dobrze wypełnił nasz formularz?\n" +  str(wartosc)
            return False
        
    except Exception:
        komunikat = "Coś poszło nie tak..."
        return False


