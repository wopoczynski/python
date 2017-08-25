def czescWspolna(s1,s2):
    tmp = []
    for e in s1:
        if (e in s2) and (e not in tmp):
            tmp.append(e)
    return tmp

def najmniejszyMianownik(mian1,mian2):
    wspolny = mian1*mian2
    wielokrot1 = []
    wielokrot2 = []
    tmp = mian1
    while tmp<wspolny:
        tmp+=mian1
        wielokrot1.append(tmp)
    tmp = mian2
    while tmp<wspolny:
        tmp+=mian2
        wielokrot2.append(tmp)
##    print(wielokrot1)
##    print(wielokrot2)
    wspolneMianowniki = czescWspolna(wielokrot1, wielokrot2)
##    return wspolneMianowniki
    return min(wspolneMianowniki)
    
    

wsp=najmniejszyMianownik(6,9)
print(wsp)
    
