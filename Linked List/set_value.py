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
    
    def get(self, index):
        if(index < 0 or index >= self.length):
            return None
        temp = self.head     
        for _ in range(index):
                temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


# create linked list
print('Create Linked List w 1 item')
my_linked_list = LinkedList(4)

# append
print('Append 3 item')
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.print_list()


# set value
print('set value at index 2')
print(my_linked_list.set_value(2, 10))
print('print list')
my_linked_list.print_list()