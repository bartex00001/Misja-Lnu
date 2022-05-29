from username_validate import username_validate
from random import randint
import re

regex_validator = re.compile("^[a-zA-Z0-9]+$")

def generateRandomUsername():
    username_parts = {
        "pre": ["Abc","De/g","Pbe","Emd","Apl", "&*a"],
        "mid": ["ole","el=e","bre","+b0e","wum", "re#"],
        "suf": ["012","10,0","000","19&1","233", "#2!!"],
    }
    a, b, c = randint(0,5), randint(0,5), randint(0,5)
    return username_parts["pre"][a] + username_parts["mid"][b] + username_parts["suf"][c]


def test():
    random_test = generateRandomUsername()

    try:
        wartosc = username_validate(random_test)
        oczekiwana = regex_validator.match(random_test)
        komunikat = f"username_validate( {random_test} ) = { str(wartosc) }; Poprawne: { bool(oczekiwana)  }"
        return wartosc == oczekiwana
    except:
        komunikat = "Coś poszło nie tak..."
        return False

test()
