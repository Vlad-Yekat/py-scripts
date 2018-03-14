class BinaryTree:
    def __init__(self):
        self.tree = EmptyNode()
    def __repr__(self):
        return repr(self.tree)
    def lookup(self,value):
        return self.tree.lookup(value)
    def insert(self,value):
        self.tree = self.tree.insert(value)

class EmptyNode:
    def __repr__(self):
        return '*'
    def lookup(self,value):
        return False
    def insert(self,value):
        return BinaryNode(self,value,self)

class BinaryNode:
    def __init__(self,left,value,right):
        self.data = value
        self.left = left
        self.right = right

    def lookup(self,value):
        if self.data == value:
            return True
        elif self.data > value:
            return self.left.lookup(value)
        else:
            return self.right.lookup(value)

    def insert(self,value):
        if self.data > value:
            self.left = self.left.insert(value)
        elif self.data < value:
            self.right = self.right.insert(value)
        return self

    def __repr__(self):
        return ('(%s, %s, %s)' % (repr(self.left),repr(self.data),repr(self.right)))

x = BinaryTree()
print(x)
x.insert(1)
print(x)
x.insert(2)
print(x)
x.insert(0)
print(x)
x.insert(3)
print(x)