#ciag fibbonaciego

def fibbonaci(n):
    wynik=[0]
    f1=0
    f2=1
    for l in range(1,n):
        fn=f1+f2
        wynik.append(fn)
        f1=f2
        f2=fn
    return wynik
a=fibbonaci(98367)
print(a)


#metoda druga
def fib2(n):
    f=[0,1]
    i=2
    while n>=i:
        f2=f[i-1]+f[i-2]
        f.append([f2])
        i+=1
    return f
