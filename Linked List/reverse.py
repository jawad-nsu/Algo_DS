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
        if(index < 0 or index >= self.length):
            return None
        temp = self.head     
        for _ in range(index):
                temp = temp.next
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        pre_temp = None
        post_temp = temp.next
        for _ in range(self.length):
            post_temp = temp.next
            temp.next = pre_temp
            pre_temp = temp  
            temp = post_temp

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

# reverse
print('reverse linked list')
my_linked_list.reverse()
my_linked_list.print_list()
