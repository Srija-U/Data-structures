class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def dequeue(self):
        if len(self.s1)==0:
            print("QUEUE IS EMPTY")
        x=self.s1.pop()
        return x

q=queue()
while True:
    print("1.Enqueue   2.Dequeue   3.print   4.exit")
    c=int(input())
    if c==1:
        print("Enter the value to enqueue")
        x=int(input())
        q.enqueue(x)
        print()
        print("ELEMENT INSERTED")
        print()
    elif c==2:
        print()
        print("POPPED ELEMENT: ",end="")
        print(q.dequeue())
        print()
    elif c==3:
        print(*q.s1)
    elif c==4:
        exit()
    else:
        print("INVALID!!")
        
            
