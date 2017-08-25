def tablica (m,n):        
    T=[]
    for e in range(0,m):
        W=[]
        for j in range(0,n):
            W.append(0)
        T.append(W)
    return T


def wypisz(tab):      
    for i in tab:
        print("".join(str(i)))
def wstaw(tablica,liczba,m,n):
    if tablica[m][n]==0:
        tablica[m][n]=liczba
        return True

    return False     
def wypelnijwiersz(tablica,liczba,wiersz,nadpisz=False):
    m=len(tablica[0])
    for i in range(0,m):
        if tablica[wiersz][i]==0 or nadpisz:
            tablica[wiersz][i]=liczba
        
def wypelnijkolumne(tablica,liczba,kolumna,nadpisz=False):
    m=len(tablica[kolumna])
    for i in range (0,m):
        if tablica[kolumna][i]==0 or nadpisz:
            tablica[i][kolumna]=liczba

def wypelnijprzekatna(tablica,liczba,nadpisz=False):
    i=0
    j=0
    x=len(tablica)
    y=len(tablica[0])
    while i<x and j<y:        
        if tablica[i][j]==0 or nadpisz:
            tablica[i][j]=liczba
        i+=1
        j+=1
def wypelnijtablice(tablica,liczba, nadpisz=False):
    n=len(tablica)
    m=len(tablica[0])
    for i in range (0,n):
        for j in range(0,m):
            tablica[i][j]=liczba
        
tab=tablica(10,8)
wstaw(tab,6,4,4)
wypelnijwiersz(tab,1,0)
wypelnijkolumne(tab,2,5)
wypelnijprzekatna(tab,3)
wypisz (tab)

wypelnijtablice(tab,6)
wypisz(tab)
