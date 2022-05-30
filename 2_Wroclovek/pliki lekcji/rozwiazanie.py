def reszta(zaplacona_kwota, ilosc_magnesow, ilosc_dlugopisow, ilosc_pocztowek, ilosc_figurek):
    koszt_magnesu = 5.40
    koszt_długopisu = 3.49
    koszt_pocztowki = 2.99
    koszt_figurki_krasnala = 10.35

    return round(zaplacona_kwota - (ilosc_magnesow*koszt_magnesu + ilosc_dlugopisow*koszt_długopisu + ilosc_pocztowek*koszt_pocztowki + ilosc_figurek*koszt_figurki_krasnala), 2)
