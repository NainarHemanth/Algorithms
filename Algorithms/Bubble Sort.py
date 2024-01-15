def bubbleSort(l):
    for i in range(len(l)):
        for j in range(0,len(l)):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
    return l

a = list(map(int,input().split()))
print(bubbleSort(a))