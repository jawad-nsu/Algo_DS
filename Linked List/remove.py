class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
            self.tail = new_node    
        self.length += 1
        return True
    
    def pop(self):
        temp = None
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            iterate = self.head
            while iterate.next != self.tail:
                iterate = iterate.next
            temp = iterate.next 
            iterate.next = None
            self.tail = iterate
            self.length -= 1
            return temp

    def pop_first(self):
        temp = None
        if self.length == 0:
            pass 
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            self.head = temp.next
            self.length -= 1
            
        return temp

    def remove(self, index):
        if(index < 0 or index >= self.length):
            return None
        elif(index == 0):
            return self.pop_first()
        elif(index == self.length-1):
            return self.pop()
        else:
            prev = self.get(index-1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp
        
    def get(self, index):
        if(index < 0 or index >= self.length):
            return None
        temp = self.head     
        for _ in range(index):
                temp = temp.next
        return temp
        
# create linked list
print('Create Linked List w 1 item')
my_linked_list = LinkedList(4)
my_linked_list.print_list()

# append
print('Append 3 items')
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.print_list()

# remove
print('Remove item at index 1')
print(my_linked_list.remove(1).value)
print('Print list')
my_linked_list.print_list()