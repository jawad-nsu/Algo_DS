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
        
            

            
