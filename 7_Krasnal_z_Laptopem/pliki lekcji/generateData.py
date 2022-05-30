import random

def ranel(ls):
    return ls[random.randint(0, len(ls)-1)]


data = 'CREATE TABLE Uzytkownicy (id INTEGER PRIMARY KEY, imie TEXT NOT NULL, nazwisko TEXT NOT NULL, wiek INTEGER, pesel TEXT NOT NULL);\n'

names = [ "Jurek", "Tomek", "Andrzej", "Jan", "Michał", 
"Bartek", "Konstanty", "Bolesław", "Włodzimierz", "Antoni" ]

lastnames = [ "Owsiak", "Powolny", "Kącki", "Stanisławski", "Muc", "Kaczyński", "Baczyński",
"Huk", "Ziaja"]

for i in range(0, 100):
    if ( i == 45 ):
        name = ranel(names)
        lastname = ranel(lastnames)
        age = random.randint(19, 39)
        pesel = "15 OR 1 = 1"
        data += f"INSERT INTO Uzytkownicy VALUES({i},'{name}','{lastname}',{age},'{pesel}');\n"
        continue
    name = ranel(names)
    lastname = ranel(lastnames)
    age = random.randint(19, 39)
    pesel = random.randint(10000000000, 40000000000)
    data += f"INSERT INTO Uzytkownicy VALUES({i},'{name}','{lastname}',{age},'{pesel}');\n"

with open("data.csv", "w+", encoding="utf8") as file:
    file.write(data)