#Kadane's algorithm
def maxsumsubarray(arr,size):
    max_so_far = 0
    max_end = 0
    start =0
    end=0
    s=0
    for i in range(size):
        max_end += a[i]
        if (max_so_far<max_end):
            max_so_far = max_end
            start=s
            end=i
        if (max_end<0):
            max_end=0
            s=i+1
    print("maximum subarray sum is: ",max_so_far)
    print("starting index is: ",s)
    print("ending index is: ",end)
            
            
a = list(map(int,input().split()))

si=len(a)
maxsumsubarray(a,si)