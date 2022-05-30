import datetime


def wiek(krasnale):
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