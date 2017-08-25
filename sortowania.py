import time, math

def bubbleSort(L):    
    licznik = 0
    while True:
        posortowane = True
        for i in range(0,len(L)-1): 
            if L[i]>L[i+1]:
                tmp=L[i]
                L[i]=L[i+1]
                L[i+1]=tmp

                posortowane = False

        if posortowane:
            break
    return L
[0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
def insertionSort(L):
    for index in range(1,len(L)): 
        element = L[index]      
        miejsce = index               
        while miejsce>0 and L[miejsce-1]>element:
            L[miejsce]=L[miejsce-1]
            miejsce = miejsce-1
        L[miejsce]=element
    return L


def quickSort(L):
    if len(L)<=0:
        return L
    
    maks = max(L)
    mini = min(L)
    pivot = mini+(maks-mini)/2

    mniejsze=[]
    rowne=[]
    wieksze=[]
    for x in L:
        if x>pivot:
            wieksze.append(x)
        elif x<pivot:
            mniejsze.append(x)
        else:
            rowne.append(x)
    
    return  quickSort(mniejsze) + rowne + quickSort(wieksze)



def merge(L,start, center,finish):
	"""Operacja scalania"""
	i = start
	j = center + 1

	L2 = [] 

	while (i <= center) and (j <= finish):
		if L[j] < L[i]:	
			L2.append(L[j])
			j = j + 1
		else:
			L2.append(L[i])
			i = i + 1
				
	if i <= center:
		while i <= center:
			L2.append(L[i])
			i = i + 1
	else:
		while j <= finish:
			L2.append(L[j])
			j = j + 1

	s = finish - start + 1
	i = 0
	while i < s:
		L[start + i] = L2[i]
		i = i + 1

	return L


def mergeSort(L):
    return merge_sort(L,0,len(L)-1)

def merge_sort(L, start, finish):
	"""sortowanie merge sort"""
	if start != finish:
		
		center = int(math.floor((start + finish)/2))
		merge_sort(L, start, center)
		merge_sort(L,center+1,finish)
		merge(L,start, center,finish)
	return L

if __name__=='__main__':
    print('Wykonanie testowe modułu')
    posortowany = [0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]

    wek=[0,2,1,2,3,2,3,4,5,4,3,2]
    wek=insertionSort(wek)
    if wek == posortowany:
        print('Test OK (InsertionSort function)')
    else:
        print('Faliure!!! (InsertionSort function)')
        
    wek=[0,2,1,2,3,2,3,4,5,4,3,2]
    wek=bubbleSort(wek)
    if wek == posortowany:
        print('Test OK (sortowanie_babelkowe function)')
    else:
        print('Faliure!!! (sortowanie_babelkowe function)')

    wek=[0,2,1,2,3,2,3,4,5,4,3,2]
    wek=quickSort(wek)
    if wek == posortowany:
        print('Test OK (quicksort function)')
    else:
        print('Faliure!!! (quicksort function)')
        
    wek=[0,2,1,2,3,2,3,4,5,4,3,2]
    wek=mergeSort(wek)
    if wek == posortowany:
        print('Test OK (merge_sort function)')
    else:
        print('Faliure!!! (merge_sort function)')

    print('\nPreforming efficiency test...\n')
    dlugosc = 1000


    wektor=list(range(1,dlugosc))
    wektor.reverse()
    start = time.time()
    insertionSort(wektor)
    stop = time.time()
    print('Insertion Sort: ' + str(stop-start))  


    wektor=list(range(1,dlugosc))
    wektor.reverse()
    start = time.time()
    bubbleSort(wektor)
    stop = time.time()
    print('Bubble sort: ' + str(stop-start))       

    wektor=list(range(1,dlugosc))
    wektor.reverse()
    start = time.time()
    wektor = quickSort(wektor)
    stop = time.time()
    print('Quick Sort: ' + str(stop-start))

    wektor=list(range(1,dlugosc))
    wektor.reverse()
    start = time.time()
    wektor = mergeSort(wektor)
    stop = time.time()
    print('Mergre Sort: ' + str(stop-start)) 

    wektor=list(range(1,dlugosc))
    wektor.reverse()
    start = time.time()
    wektor.sort()
    stop = time.time()
    print('List.sort(): ' + str(stop-start))


