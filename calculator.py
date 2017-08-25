import math

while True:
    x = input('Podaj x = ')
    x = float(x)
    wybor = input('Wartość którego wzoru chcesz policzyć (1-6)? ')
    if wybor.isnumeric():
        wybor=int(wybor)
        if wybor==1:
            w1 = 1/3
            print('w1 = ' + str(w1))
        elif wybor == 2:
            w2 = 2*math.sqrt(x+3)
            print('w2 = ' + str(w2))
        elif wybor == 3:
            w3 = 1/(x*x+x-6)
            print('w3 = ' + str(w3))
        elif wybor == 4:
            w4 = 1/(math.pow(x,3)-2*math.pow(x,2)-23*x+60)
            print('w4 = ' + str(w4))
        elif wybor == 5:
            w5 = abs(x)
            print('w5 = ' + str(w5))
        elif wybor == 2:
            w6 = math.e + math.exp(x) + math.sin(x)
            print('w6 = ' + str(w6))
        else:
            print('Nieznany wybor')
    else:
        print('Eeeee?')
    decyzja = input('Kontynuowac? (T/N)')
    if decyzja.lower()=='n':
        break

print('Do widzenia...')
