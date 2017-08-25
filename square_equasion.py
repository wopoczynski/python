from math import sqrt
def RowKwa(a,b,c):
    wynik=[]
    delta=(b**2-4*a*c)
    if delta>0:
        x1=(-b-sqrt(delta))/(2*a)
        wynik.append(x1)
        x2=(-b+sqrt(delta))/(2*a)
        wynik.append(x2)
    if detla==0:
        x=(-b)/(2*a)
        wynik.append(x)
    if delta<0:
        print('pierwiastki nierzeczywiste')
    return wynik


a=float(input('podaj parametr a: '))
b=float(input('podaj parametr b: '))
c=float(input('podaj parametr c: '))
wynik=RowKwa(a,b,c)
print('pierwiastki to: ',wynik)
