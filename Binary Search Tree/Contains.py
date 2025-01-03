class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BST():
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        
        temp = self.root
        while (True):
            if temp.value == value:
                return False
            
            if temp.value < value:
                if temp.left is None:
                    temp.left = Node(value)
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = Node(value)
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        
        return False
            

my_tree = BST()
my_tree.insert(2)        
my_tree.insert(1)        
my_tree.insert(3)

print(my_tree.root.value)        
print(my_tree.root.left.value)        
print(my_tree.root.right.value)

print(my_tree.contains(2))
print(my_tree.contains(7))
