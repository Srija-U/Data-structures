class st:
    def __init__(self):
        self.s1=[]
        self.s2=[]
        self.top=-1
    def push(self,x):
        if(self.top==-1):
            self.top=0
            self.s1.append(x)
            print("INSERTED ELEMENT: ",x)
        else:
            self.top+=1
            self.s1.append(x)
            print("INSERTED ELEMENT: ",x)
    def rev(self):
        while len(self.s1)!=0:
            t=self.s1.pop()
            self.s2.append(t)
        self.s1=self.s2
        self.s2=[]
o=st()
o.push(1)
o.push(2)
o.push(3)
o.push(4)
print("BEFORE REVERSE: ",*o.s1)
o.rev()
print("AFTER REVERSE:  ",*o.s1)

