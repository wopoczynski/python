global licznik

licznik = 0

def hanoi(n,z='1',do='2',tmp='3'):
    global licznik
    
    if n==1:
        licznik += 1
        print('Krok %5d' % licznik +': Przenieś z słupka ' + str(z) + ' na słupek '+str(do))
    else:
        hanoi(n-1,z,tmp,do) 
        hanoi(1,z,do,tmp)
        hanoi(n-1,tmp,do,z)


hanoi(5)
