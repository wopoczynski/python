# płytoteka
import pickle

def wprowadzAlbum():
    pass

def zapiszDoPliku(baza):
    pickle.dump(baza, open('baza.p', 'wb' ) )

def zaladujZPliku():
    baza = pickle.load(open('baza.p','rb'))
    return baza

def dodajAlbumDoBazy(baza,album):
    pass

def nowyIndeks(baza):
    pass

def usunAlbumZBazy(baza):
    pass
    

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
    pass

def wypiszAlbum(album):
    pass


# tworzymy słownik, który będzie używany w programie
b = {}
# główna pętla programu
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
        
            
        
        
    
    
