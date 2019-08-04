def sear(n,l,low,high,k):
    if low<high:
        mid=int((low+high)/2)
        if l[mid]==k:
            return mid+1
        elif k<l[mid]:
            return sear(n,l,low,(mid-1),k)
        else:
            return sear(n,l,(mid+1),high,k)
    return None
n=int(input())
l=[int(i) for i in input().split()]
k=int(input())
print(sear(n,l,0,(n-1),k))
