class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def atbeg(self,newval):
        newnode=node(newval)
        newnode.next=self.head
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode
    def atend(self,newval):
        newnode=node(newval)
        last=self.head
        while last.next is not None:
            last=last.next
        newnode.prev=last
        last.next=newnode
    def btw(self,middle,newval):
        newnode=node(newval)
        m=self.head
        while m.next:
            if m.data==middle:
                break
            else:
                last=m
                m=m.next
        newnode.prev=m
        newnode.next=m.next
        m.next=newnode
        m=m.next
        m.prev=newnode
    def rem(self,val):
        last=self.head
        while last.data!=val:
            temp=last
            last=last.next
        temp.next=last.next
        last.prev=temp
    def listprint(self):
        last=self.head
        while last is not None:
            print(last.data)
            last=last.next
    def count(self):
        last=self.head
        c=0
        while(last is not None):
            c+=1
            last=last.next
        return c
obj=dll()
obj.atbeg(5)
obj.atbeg(4)
print("ATBEG OF 5 AND 4:")
obj.listprint()
print("Count: ",obj.count())
obj.btw(2,3)
print("Between of 2 and 3")
obj.listprint()
print("Count: ",obj.count())
obj.atend(2)
obj.atend(1)
print("ATEND OF 2 AND 1")
obj.listprint()
print("Count: ",obj.count())
obj.rem(2)
print("Remove: 2")
obj.listprint()
print("Count: ",obj.count())
