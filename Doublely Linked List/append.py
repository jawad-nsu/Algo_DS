class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublelyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)
        
        if self.length < 1:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.tail
            new_node.prev = self.head
        else: 
            
        
