class cq:
    def __init__(self,capacity):
        self.q=[]
        self.capacity=capacity
        self.front=-1
        self.rear=-1
    def enqueue(self,x):
        if self.front==(self.rear+1)%self.capacity:
            print("QUEUE IS FULL")
        elif self.front==-1:
            self.front=0
            self.q.append(x)
            print("ELEMENT IS INSERTED ",x)
            self.rear=0
        else:
            self.rear+=1
            self.q.append(x)
            print("ELEMENT IS INSERTED ",x)
    def dequeue(self):
        if(self.front<=self.rear):
            if self.front==-1:
                print("QUEUE IS EMPTY")
            elif self.rear==0:
                self.front=-1
                t=self.q.pop()
                self.rear=-1
                print("POPPED ELEMENT: ",t)
                return
            else:
                self.front+=1
                t=self.q.pop(0)
                print("POPPED ELEMENT: ",t)
        else:
            print("QUEUE IS EMPTY")
    def fr(self):
        print("FRONT: ",self.front)
        print("REAR:  ",self.rear)
c=cq(3)
c.enqueue(1)
c.fr()
c.enqueue(2)
c.fr()
c.enqueue(3)
c.fr()
c.enqueue(4)
c.fr()
print(*c.q)
c.dequeue()
c.fr()
c.dequeue()
c.fr()
c.dequeue()
c.fr()
c.dequeue()
c.fr()
