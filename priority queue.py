class pq:
    def __init__(self,capacity):
        self.q=[]
        self.capacity=capacity
        self.front=-1
        self.rear=-1        
    def enqueue(self,x):
        if self.rear==self.capacity-1:
            print("QUEUE IS FULL")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.q.append(x)
            print("ELEMENT INSERTED: ",x)
        else:
            self.q.append(x)
            self.rear+=1
            print("ELEMENT INSERTED: ",x)
    def dequeue(self):
        if self.rear==-1:
            print("QUEUE IS EMPTY")
            return
        else:
            t=max(self.q)
            te=self.q.index(t)
            self.q.remove(t)
            self.rear=len(self.q)-1
            print("POPPED ELEMENT: ",t)
o=pq(5)
o.enqueue(1)
o.enqueue(2)
o.enqueue(3)
o.enqueue(5)
o.enqueue(4)
o.enqueue(6)
print(*o.q)
o.dequeue()
o.dequeue()
o.dequeue()
o.dequeue()
o.dequeue()
o.dequeue()
