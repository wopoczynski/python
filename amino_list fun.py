import time, random

print('Generuję losowe DNA!')
rozpoczecie = time.clock()
Namino = 1000000
S1=''

Podziel = 1000
ile = int(Namino/Podziel)
for i in range(1,3*ile+1):
    S1 = S1 + random.choice(['A', 'U', 'G', 'C'])
S1 = S1 * Podziel
zakonczenie = time.clock()
czas = zakonczenie - rozpoczecie
print('Czas trwania generacji = %6.3f sekund' % czas)


dlugosc = len(S1)
n_amino = dlugosc // 3
reszta = dlugosc % 3

amino = []

print('Ilość aminokwasów = ' + str(n_amino))
print('Reszta = ' + str(reszta))

sekwencje =['UUU',
          'UUC',
          'UUA',
          'UUG',
          
          'CUU',
          'CUC',
          'CUA',
          'CUG',
          
          'AUU',
          'AUC',
          'AUA',
          'AUG',
          
          'GUU',
          'GUC',
          'GUA',
          'GUG',
          
          'UCU',
          'UCC',
          'UCA',
          'UCG',
          
          'CCU',
          'CCC',
          'CCA',
          'CCG',
          
          'ACU',
          'ACC',
          'ACA',
          'ACG',

          'GCU',
          'GCC',
          'GCA',
          'GCG',
          
          'UAU',
          'UAC',
          'UAA',
          'UAG',
          
          'CAU',
          'CAC',
          'CAA',
          'CAG',
          
          'AAU',
          'AAC',
          'AAA',
          'AAG',
          
          'GAU',
          'GAC',
          'GAA',
          'GAG',
          
          'UGU',
          'UGC',
          'UGA',
          'UGG',
          
          'CGU',
          'CGC',
          'CGA',
          'CGG',
          
          'AGU',
          'AGC',
          'AGA',
          'AGG',
          
          'GGU',
          'GGC',
          'GGA',
          'GGG']

aminokwasy = ['Phe',
       'Phe',
       'Leu',
       'Leu',
          
       'Leu',
       'Leu',
       'Leu',
       'Leu',
          
       'Ile',
       'Ile',
       'Ile',
       'Met (START)',
          
       'Val',
       'Val',
       'Val',
       'Val',
          
       'Ser',
       'Ser',
       'Ser',
       'Ser',
          
       'Pro',
       'Pro',
       'Pro',
       'Pro',
          
       'Thr',
       'Thr',
       'Thr',
       'Thr',

       'Ala',
       'Ala',
       'Ala',
       'Ala',
          
       'Tyr',
       'Tyr',
       'Stop',
       'Stop',
          
       'His',
       'His',
       'Gln',
       'Gln',
          
       'Asn',
       'Asn',
       'Lys',
       'Lys',
          
       'Asp',
       'Asp',
       'Glu',
       'Glu',
          
       'Tyr',
       'Cys',
       'Cys',
       'Trp',
          
       'Arg',
       'Arg',
       'Arg',
       'Arg',
          
       'Ser',
       'Ser',
       'Arg',
       'Arg',
          
       'Gly',
       'Gly',
       'Gly',
       'Gly']

rozpoczecie = time.clock()

for i in range(0,n_amino):
    sek = S1[3*i:3*i+3]

    index = 0
    for s in sekwencje:
        if s == sek:
            amino.append(aminokwasy[index])
            break
        else:
            index += 1

    
zakonczenie = time.clock()
print('Job done!')
print(len(amino))
czas = zakonczenie - rozpoczecie
print('Czas trwania generacji = %6.3f sekund' % czas)
