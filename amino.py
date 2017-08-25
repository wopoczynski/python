import time, random

S1 = list('AUGGGCCGGUUAAAUUAUGCGGCCAAUUAG')*10


dlugosc= len(S1)
n_amino= dlugosc // 3
reszta= dlugosc % 3

amino = []

print('Ilość aminokwasów = ' + str(n_amino))
print('Reszta = ' + str(reszta))

rozpoczecie = time.clock()

for i in range(0,n_amino):
    sek = S1[3*i:3*i+3]
    print(sek)

    if sek[0]=='G':
        if sek[1]=='G':
            if sek[2]=='G':
                amino.append('Gly')
            elif sek[2]=='U':
                amino.append('Gly')
            elif sek[2]=='C':
                amino.append('Gly')
            elif sek[2]=='A':
                amino.append('Gly')
            else:
                print('Error')
                break
        elif sek[1]=='U':
            if sek[2]=='G':
                amino.append('Val')
            elif sek[2]=='U':
                amino.append('Val')
            elif sek[2]=='C':
                amino.append('Val')
            elif sek[2]=='A':
                amino.append('Val')
            else:
                print('Error')
                break
        elif sek[1]=='C':
            if sek[2]=='G':
                amino.append('Ala')
            elif sek[2]=='U':
                amino.append('Ala')
            elif sek[2]=='C':
                amino.append('Ala')
            elif sek[2]=='A':
                amino.append('Ala')
            else:
                print('Error')
                break
        elif sek[1]=='A':
            if sek[2]=='G':
                amino.append('Glu')
            elif sek[2]=='U':
                amino.append('Asp')
            elif sek[2]=='C':
                amino.append('Asp')
            elif sek[2]=='A':
                amino.append('Glu')
            else:
                print('Error')
                break
        else:
            print('Error')
            break            
    elif sek[0]=='U':
        if sek[1]=='G':
            if sek[2]=='G':
                amino.append('Trp')
            elif sek[2]=='U':
                amino.append('Cys')
            elif sek[2]=='C':
                amino.append('Cys')
            elif sek[2]=='A':
                amino.append('STOP')
            else:
                print('Error')
                break
        elif sek[1]=='U':
            if sek[2]=='G':
                amino.append('Leu')
            elif sek[2]=='U':
                amino.append('Phe')
            elif sek[2]=='C':
                amino.append('Phe')
            elif sek[2]=='A':
                amino.append('Leu')
            else:
                print('Error')
                break
        elif sek[1]=='C':
            if sek[2]=='G':
                amino.append('Ser')
            elif sek[2]=='U':
                amino.append('Ser')
            elif sek[2]=='C':
                amino.append('Ser')
            elif sek[2]=='A':
                amino.append('Ser')
            else:
                print('Error')
                break
        elif sek[1]=='A':
            if sek[2]=='G':
                amino.append('STOP')
            elif sek[2]=='U':
                amino.append('Tyr')
            elif sek[2]=='C':
                amino.append('Tyr')
            elif sek[2]=='A':
                amino.append('STOP')
            else:
                print('Error')
                break
        else:
            print('Error')
            break    
    elif sek[0]=='C':
        if sek[1]=='G':
            if sek[2]=='G':
                amino.append('Arg')
            elif sek[2]=='U':
                amino.append('Arg')
            elif sek[2]=='C':
                amino.append('Arg')
            elif sek[2]=='A':
                amino.append('Arg')
            else:
                print('Error')
                break
        elif sek[1]=='U':
            if sek[2]=='G':
                amino.append('Leu')
            elif sek[2]=='U':
                amino.append('Leu')
            elif sek[2]=='C':
                amino.append('Leu')
            elif sek[2]=='A':
                amino.append('Leu')
            else:
                print('Error')
                break
        elif sek[1]=='C':
            if sek[2]=='G':
                amino.append('Pro')
            elif sek[2]=='U':
                amino.append('Pro')
            elif sek[2]=='C':
                amino.append('Pro')
            elif sek[2]=='A':
                amino.append('A')
            else:
                print('Error')
                break
        elif sek[1]=='A':
            if sek[2]=='G':
                amino.append('Gln')
            elif sek[2]=='U':
                amino.append('His')
            elif sek[2]=='C':
                amino.append('His')
            elif sek[2]=='A':
                amino.append('Gln')
            else:
                print('Error')
                break
        else:
            print('Error')
            break    
    elif sek[0]=='A':
        if sek[1]=='G':
            if sek[2]=='G':
                amino.append('Arg')
            elif sek[2]=='U':
                amino.append('Ser')
            elif sek[2]=='C':
                amino.append('ser')
            elif sek[2]=='A':
                amino.append('Arg')
            else:
                print('Error')
                break
        elif sek[1]=='U':
            if sek[2]=='G':
                amino.append('START (Met)')
            elif sek[2]=='U':
                amino.append('Ile')
            elif sek[2]=='C':
                amino.append('Ile')
            elif sek[2]=='A':
                amino.append('Ile')
            else:
                print('Error')
                break
        elif sek[1]=='C':
            if sek[2]=='G':
                amino.append('Thr')
            elif sek[2]=='U':
                amino.append('Thr')
            elif sek[2]=='C':
                amino.append('Thr')
            elif sek[2]=='A':
                amino.append('Thr')
            else:
                print('Error')
                break
        elif sek[1]=='A':
            if sek[2]=='G':
                amino.append('Lys')
            elif sek[2]=='U':
                amino.append('Asn')
            elif sek[2]=='C':
                amino.append('Asn')
            elif sek[2]=='A':
                amino.append('Lys')
            else:
                print('Error')
                break
        else:
            print('Error')
            break    
    else:
        print('Error')
        break
zakonczenie = time.clock()
print(len(amino))
czas = zakonczenie - rozpoczecie
print('Czas = %6.3f sekund' % czas)
print(amino)



