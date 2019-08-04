def push(l,n):
    if(n==len(l)):
        print()
        print("STACK IS FULL!!")
        print()
        return l
    else:
        print("Enter the value to insert")
        x=int(input())
        l.append(x)
        print("INSERTED!!")
        return l
def pop(l,n):
    if(len(l)==0):
        print()
        print("STACK IS EMPTY")
        print()
        return l
    else:
        t=l.pop()
        print("Popped element is: ",t)
        return l 
l=[]
print("Size of stack:")
n=int(input())
while 1:
    print("1.Push    2.pop    3.print    4.exit()")
    c=int(input())
    if(c==1):
        l=push(l,n)
    elif c==2:
        l=pop(l,n)
    elif c==3:
        print(*l)
    elif c==4:
        exit()
    else:
        print("INVALID!!!!")
