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
            return temp.value

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

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


# create linked list
print('Create Linked List w 1 item')
my_linked_list = LinkedList(4)
my_linked_list.print_list()

# append
print('Append 1 item')
my_linked_list.append(5)
my_linked_list.print_list()

# prepend
print('prepend 1 item')
my_linked_list.prepend(3)
my_linked_list.print_list()

# pop first
print('pop first')
print(my_linked_list.pop_first().value)
print('print list')
my_linked_list.print_list()




