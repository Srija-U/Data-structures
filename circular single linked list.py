class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linked:
    def __init__(self):
        self.head=None
    def atend(self,newdata):
        newnode=node(newdata)
        last=self.head
        newnode.next=self.head
        if self.head is None:
            newnode.next=self.head
            self.head=newnode
            return
        elif last.next is None:
            last.next=newnode
        else:
            while last.next!=self.head:
                last=last.next
            last.next=newnode
    def atbegin(self,newdata):
        newnode=node(newdata)
        newnode.next=self.head
        last=self.head
        while last.next!=self.head:
            last=last.next
        self.head=newnode
        last.next=self.head
    def listprint(self):
        printval=self.head
        while printval.next!=self.head:
            print(printval.data)
            printval=printval.next
        print(printval.data)
    def inbetween(self,middle,new):
        last=self.head
        while last.next:
            if last.data==middle:
                break
            else:
                last=last.next
        middle=last
        newnode=node(new)
        newnode.next=middle.next
        middle.next=newnode
    def rem(self,key):
        head=self.head
        if head is not None:
            if head.data==key:
                self.head=head.next
                head=None
                return
            while head is not None:
                if head.data==key:
                    break
                prev=head
                head=head.next
            if head==None:
                return
            prev.next=head.next
            head=None
    def count(self):
        last=self.head
        c=0
        while(last.next!=self.head):
            c+=1
            last=last.next
        return c+1     
lis=linked()
lis.head=node(3)
lis.atend(4)
lis.atend(6)
print("ATEND OF 4 AND 6")
lis.listprint()
print("count:",lis.count())
lis.atbegin(2)
lis.atbegin(1)
print("ATBEGIN OF 2 AND 1")
lis.listprint()
print("count:",lis.count())
print("INBETWEEN AFTER 4")
lis.inbetween(4,5)
lis.listprint()
print("count:",lis.count())
lis.rem(4)
print("AFTER REMOVING 4")
lis.listprint()
print("count:",lis.count())
