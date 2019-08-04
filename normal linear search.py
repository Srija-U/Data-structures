n=int(input())
l=[int(i) for i in input().split()]
k=int(input())
for i in range(0,n):
    if(l[i]==k):
        print("found at",i+1)
        exit()
print("Not found")
