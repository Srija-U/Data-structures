def sear(n,l,k):
    low=0
    high=n-1
    while(low<high):
        mid=int((low+high)/2)
        if l[mid]==k:
            return mid+1
        elif k<l[mid]:
            high=mid-1
        else:
            low=mid+1
    return None
n=int(input())
l=[int(i) for i in input().split()]
k=int(input())
print(sear(n,l,k))
