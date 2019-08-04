def ls(l,k,i):
    if(l[i]==k):
        return i+1
    else:
        return(ls(l,k,i+1))
n=int(input())
l=[int(i) for i in input().split()]
k=int(input())
print(ls(l,k,0))
        
