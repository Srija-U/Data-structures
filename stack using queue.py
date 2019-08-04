class stack:
    def __init__(self,capacity):
        self.q1=[]
        self.q2=[]
        self.capacity=capacity
        self.top=-1
    def push(self,x):
        if self.top==self.capacity:
            print("STACK IS FULL")
        self.q1.append(x)
        self.top+=1
        print("INSERTED ELEMENT: ",x)
    def popp(self):
        if len(self.q1)==0:
            print("STACK IS EMPTY")
            return
        if(len(self.q1)==1):
            te=self.q1.pop()
            print("POPPED ELEMENT: ",te)
        else:
            while(len(self.q1)!=1):
                t=self.q1.pop(0)
                self.q2.append(t)
            te=self.q1.pop()
            print("POPPED ELEMENT: ",te)
            while(len(self.q2)!=0):
                t=self.q2.pop(0)
                self.q1.append(t)
    def topp(self):
        if len(self.q1)==0:
            print("STACK IS EMPTY")
            return
        print(self.q1[len(self.q1)-1])
s=stack(3)
s.push(1)
s.push(2)
s.push(3)
print("The top element is ",end="")
s.topp()
s.popp()
print("The top element is ",end="")
s.topp()
s.popp()
print("The top element is ",end="")
s.topp()
s.popp()
s.popp()
