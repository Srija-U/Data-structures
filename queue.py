def enqueue(l,n):
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
def dequeue(l,n):
    if(len(l)==0):
        print()
        print("STACK IS EMPTY")
        print()
        return l
    else:
        t=l[0]
        l.remove(t)
        print("The popped element is: ",t)
        return l
l=[]
print("Size of queue")
n=int(input())
while 1:
    print()
    print("1.Enqueue   2.Dequeue   3.Print  4.Exit")
    c=int(input())
    if(c==1):
        l=enqueue(l,n)
    elif c==2:
        l=dequeue(l,n)
    elif c==3:
        print(*l)
    elif(c==4):
        exit()
