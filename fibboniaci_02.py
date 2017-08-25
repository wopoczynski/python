import time

licznik = 0
def fibbonaci(n,fib):
    global licznik

    if n in fib:
        return fib[n]
    else:        
        if n==0:
            licznik +=1
            fib[0]= 0
            return 0
        elif n==1:
            licznik +=1
            fib[1]=1
            return 1
        else:
            fib_n_1 = fibbonaci(n-1,fib)
            fib_n_2 = fibbonaci(n-2,fib)
            fib[n-1]=fib_n_1
            fib[n-2]=fib_n_2
            licznik += 1
            return fib_n_1 + fib_n_2


start=time.time()
for i in range(0,1):        
    slownik={}
    war=fibbonaci(320,slownik)
stop=time.time()
print(war)
print('Licznik: ' + str(licznik))
print('Czs obliczeń = '+str(stop-start))
