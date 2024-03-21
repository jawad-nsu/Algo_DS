class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length < 1:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def pop_first(self):
        if self.length < 1:
            return None
        
        temp = self.head 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index < self.length/2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr
        else:
            curr = self.tail
            for _ in range(self.length-1, index, -1):
                curr = curr.prev
            return curr
        

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(7)
my_doubly_linked_list.append(8)
my_doubly_linked_list.print_list()
print('get', my_doubly_linked_list.get(0).value)
print('get', my_doubly_linked_list.get(1).value)
print('get', my_doubly_linked_list.get(2).value)
print('get', my_doubly_linked_list.get(3).value)
print('get', my_doubly_linked_list.get(4).value)
print('get', my_doubly_linked_list.get(5).value)
print('get', my_doubly_linked_list.get(6).value)
print('get', my_doubly_linked_list.get(7).value)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2
    
"""
