class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end(ll, k):
    fast_pointer = ll.head
    slow_pointer = ll.head
    for i in range(k):
        if fast_pointer is None:
            return None
        fast_pointer = fast_pointer.next
    
    while fast_pointer != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next
    
    return slow_pointer
        




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

