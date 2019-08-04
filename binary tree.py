class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=node(data)
                    print("INSERTED: ",data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=node(data)
                    print("INSERTED: ",data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def search(self,val):
        if val<self.data:
            if self.left is None:
                return str(val)+" Not Found"
            return self.left.search(val)
        elif val>self.data:
            if self.right is None:
                return str(val)+"Not Found"
            return self.right.search(val)
        else:
            print(str(self.data),"is found")
    def remove(self,val):
        if self.left is None and self.right is None:
            return None
        elif self.left is None or self.right is None:
            if self.left is None:
                return self.right
            else:
                return self.left
        else:
            t=self.left.findmax()
            t.left=self.left.remove(t.data)
            t.right=self.right
            return t
    def findmax(self):
        while self is not None and self.right is not None:
            self=self.right
        return self
    def inorder(self):
        if self is None:
            return
        if self.left:
            self.left.inorder()
        print(self.data,end=' ')
        if self.right:
            self.right.inorder()
    def preorder(self):
        if self is None:
            return
        print(self.data,end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self is None:
            return
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end=" ")
    def levelprint(self,n,c):
        if c==n:
            print(self.data,end=" ")
        c=c+1
        if self.left:
            self.left.levelprint(n,c)
        if self.right:
            self.right.levelprint(n,c)
root=node(20)
root.insert(10)
root.insert(15)
root.insert(5)
root.insert(30)
root.insert(25)
root.insert(35)
print("INORDER TRAVERSAL : ",end=" ")
root.inorder()
print()
print("PREORDER TRAVERSAL : ",end=" ")
root.preorder()
print()
print("POSTORDER TRAVERSAL : ",end=" ")
root.postorder()
print()
print("LEVEL PRINT AT LEVEL 2: ",end=" ")
root.levelprint(2,0)
print()
print("SEARCH 25")
root.search(25)
print("REMOVE 25")
print((root.remove(25)).data)
