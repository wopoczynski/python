
import copy

def mediana(L):

    L=L[:]

    L.sort()
    n=len(L)
    if (n % 2) != 0:
        return L[n//2]
    else:
        i1 = (n//2)-1
        i2 = n//2
        return (L[i1]+L[i2])/2

liczby=[2,4,3,1,8,5,7,6]
print('Lista przed wywołaniem funkcji:')
print(liczby)
print('mediana = ' + str(mediana(liczby)))

print('Lista liczb po wywołaniu funkcji:')
print(liczby)
