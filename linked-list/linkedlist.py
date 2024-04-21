class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node

        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def insert_head(self,new_head):
        next_to_head = self.head
        self.head = new_head
        self.head.next = next_to_head

    def insert_at(self,position:int, new_node:Node):
        count = 1
        current_node = self.head
        while count < position:
            current_node = current_node.next
            count += 1
        # TODO: add exception for a position not available

        if current_node.next is not None:
            new_node.next = current_node.next
            # Else will keep the None value
        current_node.next = new_node


    def print_list(self):
        if self.head is None:
            print("Empty List")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

first = Node("Matthews")
second = Node("Zoe")
list1 = LinkedList()
list1.insert_end(first)
list1.insert_end(second)
third = Node("Alfred")
list1.insert_head(third)
list1.print_list()
print("Lista con insertar ne posicion")
fourth = Node("Bruce wine")
list1.insert_at(2,fourth)
list1.print_list()