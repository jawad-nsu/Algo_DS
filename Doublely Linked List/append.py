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
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
        

DLL = DoublelyLinkedList(1)
DLL.append(2)
DLL.append(3)
DLL.append(4)
DLL.append(5)
DLL.print_list()