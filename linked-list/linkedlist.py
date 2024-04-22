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

    def delete_head(self):
        self.head = self.head.next

    def insert_at(self,position:int, new_node:Node):
        if position < 0 or position > self.get_length():
            raise "invalid position"
        if position == 0:
            self.insert_head(new_node)

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

    def insert_list(self, data_list): #TODO : Not Finished
        if self.head is None:
            self.head = data_list[0]
            current = self.head
            for i in range(1,len(data_list)):
                current.next = data_list[i]
                current= current.next

    def delete_node(self):
        current = self.head
        while current.next is not None:
            if current.next.next is None:
                pre_last = current
                pre_last.next = None
            else:
                current = current.next

    def delete_at(self, position):
        if position < 0 or position >= self.get_length():
            raise "Invalid position of an element"
        if position == 0:
            self.delete_head()
        else:
            count = 0
            current = self.head
            while count < position:
                previous = current
                current = current.next
                count += 1
            if current.next is None:
                self.delete_node()
            else:
                previous.next = current.next

    def get_length(self): # TODO: I can add a len attribute to the linkedlist
        if self.head is None:
            return 0

        count = 1
        current = self.head
        while current.next is not None:
            count += 1
            current = current.next
        return count

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
fourth = Node("Bruce wayne")
list1.insert_at(2,fourth)
list1.print_list()
print("Largo de la lista: " + str(list1.get_length()))
# list1.delete_node()
list1.delete_at(0)
list1.print_list()


