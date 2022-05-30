from onp import onp
import random


OPERATORS = ("+", "-", "*", "//")

def generate_test():
    text = ""
    # Dwie pierwsze liczby wyrażenia zawsze muszą być liczbami
    text += str(random.randint(-20, 30))
    text += " "
    text += str(random.randint(-20, 30))
    number_counter = 2
    
    for _ in range(random.randint(0, 10)):                  # Wyrażenia mogą mieć losową długość
        if number_counter > 1:                              
            if random.randint(0,1):                         # 50% szans że nowy symbol będzie liczbą bądź operatorem
                text += " " + str(random.randint(-20, 30))
                number_counter += 1
            else:
                text += " " + random.choice(OPERATORS)
                number_counter -= 1
        else:                                               # Jeżeli na stosie znajdowałaby się tylko jedna liczba to trzeba dodać liczbę
            text += " " + str(random.randint(-20, 30))
            number_counter += 1

    while number_counter > 1:
        text += " " + random.choice(OPERATORS)
        number_counter -= 1

    return text

def calculate_correct_value(text):
    OPERATORS = ("+", "-", "*", "//")

    split_text = text.split()
    stos = []

    for i in split_text:
        if i not in OPERATORS:          # dodawanie na stos
            stos.append( int(i) )
        else:
            a = stos.pop()              # wykonywanie działań
            b = stos.pop()
            
            if i == "+":
                stos.append(b+a)
            elif i == "-":
                stos.append(b-a)
            elif i == "*":
                stos.append(b*a)
            elif i == "//":
                if a == 0:
                    return ZeroDivisionError
                stos.append(b//a)

    return stos[0]


def test():
    text = generate_test()
    correct_value = calculate_correct_value(text)
    komunikat = f"onp({text}) = {correct_value}: "

    try:
        value = onp(text)

        if value == correct_value:
            komunikat += "Wszystko dobrze!"
            return True
        else:
            komunikat += "Coś chyba źle policzyłeś..."
            return False
    except ZeroDivisionError:
        if correct_value == ZeroDivisionError:
            komunikat += "Błąd dzielenia przez zero"
            return True
        else:
            komunikat += "Niepoprawnie otrzymany błąd dzielenia przez zero"
            return False
    except Exception:
        komunikat = "Coś poszło nie tak..."
        return False
