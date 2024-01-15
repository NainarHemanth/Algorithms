def selectionSort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos =i
        l[start],l[minpos] = l[minpos],l[start]
    
    return l

a = list(map(int,input("Enter").split()))
print(selectionSort(a))
