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
         
my_linked_list = LinkedList(4)
my_linked_list.print_list()

my_linked_list.append(5)

my_linked_list.print_list()

# pop
print('after 1st popping')
print(my_linked_list.pop())
my_linked_list.print_list()

print('after 2nd popping')
print(my_linked_list.pop())
my_linked_list.print_list()

print('after 3rd popping')
print(my_linked_list.pop())
my_linked_list.print_list()





