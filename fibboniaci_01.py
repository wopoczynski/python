import time

licznik = 0

def fibbonaci(n):
    global licznik
    
    if n==0:
        licznik +=1
        return 0
    elif n==1:
        licznik +=1
        return 1
    else:
        licznik +=1
        return fibbonaci(n-1)+fibbonaci(n-2)

start=time.time()
for i in range(0,1):        
    slownik={}
    war=fibbonaci(32)
stop=time.time()
print(war)
print('Licznik: ' + str(licznik))
print('Czs obliczeń = '+str(stop-start))
