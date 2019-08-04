class node:
    def __init__(self,newval):
        self.data=newval
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def atbeg(self,newval):
        newnode=node(newval)
        last=self.head
        if self.head is None:
            self.head=newnode
            self.head.prev=self.head
            self.head.next=self.head
            return
        if last.next is self.head:
            self.head.next=newnode
            newnode.next=self.head
            self.head=newnode
            return
        while last.next is not self.head:
            last=last.next
        last.next=newnode
        newnode.next=self.head
        self.head=newnode
    def atend(self,newval):
        newnode=node(newval)
        last=self.head
        while last.next is not self.head:
            last=last.next
        last.next=newnode
        newnode.prev=last
        newnode.next=self.head
        self.head.prev=newnode
    def btw(self,middle,newval):
        newnode=node(newval)
        last=self.head
        while last.data==middle:
            temp=last
            last=last.next
        temp.next=newnode
        newnode.prev=temp
        newnode.next=last
        last.prev=newnode
    def rem(self,val):
        last=self.head
        while last.data!=val:
            tem=last
            last=last.next
        tem.next=last.next
        last.next.prev=tem
    def listprint(self):
        last=self.head
        print(last.data)
        last=last.next
        while last is not self.head:
            print(last.data)
            last=last.next
    def count(self):
        last=self.head
        c=1
        while last.next is not self.head:
            c=c+1
            last=last.next
        return c
obj=dll()
obj.atbeg(4)
obj.atbeg(3)
obj.atbeg(1)
print("ATBEG OF 4 AND 3 AND 1")
obj.listprint()
print("COUNT: ",obj.count())
obj.atend(5)
obj.atend(6)
print("ATEND OF 5 AND 6")
obj.listprint()
print("COUNT: ",obj.count())
obj.btw(1,2)
print("BETWEEN 1 AND 2")
obj.listprint()
print("COUNT: ",obj.count())
obj.rem(6)
print("REMOVE 6")
obj.listprint()
print("COUNT: ",obj.count())
