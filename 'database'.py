import pickle
def zapiszDoPliku(baza):
    pickle.dump(baza, open('baza.p', 'wb' ) )
def zaladujZPliku():
    baza = pickle.load(open('baza.p','rb'))
    return baza


def wprowadzAlbum():
    Tytul = input('Podaj Tytuł Albumu: ')
    Autor = input('Podaj Autora: ')
    IleUtworow = int(input('Podaj liczbe utworow: '))
    Utwory=[]
    for i in range(1,IleUtworow+1):
        a=input('podaj '+str(i)+ 'tytul utworu: ')
        Utwory.append(a)
    Rok=int(input('Podaj Rok Wydania Albumu: '))
    Album=(Autor, Tytul, Rok, Utwory)
    return Album

def dodajAlbumDoBazy(baza,album):
    indeks=nowyIndeks(baza)
    baza[indeks]=album

def nowyIndeks(baza):
    if len(baza)==0:
        maxx=0
    else:
        indeks=baza.keys()
        maxx=max(indeks)
    return maxx+1

def usunAlbumZBazy(baza):
    indeks=int(input('podaj ktory ma zostac usuniety: '))

    if indeks in baza:
        print('Wpis do bazy: ')
        print (b[indeks])
        decyzja=input('Czy na pewno chcesz usunąć? [t/n]')
        if decyzja.upper()=="T":
            del baza[indeks]
        else:
            print('Brak Wpisu W Bazie')

def wyborOpcji():
    print('Wybierz opcję:')
    print('1. Załaduj z pliku')
    print('2. Zapisz do pliku')
    print('3. Wypisz całą bibliotekę')
    print('4. Dodaj album')
    print('5. Usuń album')
    print('6. Wyszukaj...')
    print('0. Koniec')
    opcja = input('Wybierz polecenie: ...')
    return int(opcja)

def wyborWyszukania():
    pass
    

def wypiszKrotkieInfo(baza):    
    pass

def wypiszBaze(baza):
    print(baza)

def wypiszAlbum(album):
    pass


b = {}
while True:
    wypiszKrotkieInfo(b)
          
    opcja = wyborOpcji()
    if opcja == 0:
        break
    elif opcja == 1:
        b = zaladujZPliku()
    elif opcja == 2:
        zapiszDoPliku(b)
    elif opcja == 3:
        wypiszBaze(b)
    elif opcja == 4:
        album = wprowadzAlbum()
        dodajAlbumDoBazy(b,album)
    elif opcja ==5:
        usunAlbumZBazy(b)
    else:
        pass
