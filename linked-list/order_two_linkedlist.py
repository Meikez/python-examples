from linkedlist import LinkedList,Node

list1 = LinkedList()
list2 = LinkedList()
first_num = Node(1)
second_num = Node(2)
third_num = Node(3)
fourth_num = Node(4)

list1.insert_end(second_num)
list1.insert_end(fourth_num)
list1.insert_end(first_num)
list1.insert_end(third_num)

print("Lista 1 :")
list1.print_list()
# Crear nodos para la lista2 si uso las variables de los nodos anteriores daria problemas como un bucle infinito en el while
first_num_list2 = Node(1)  # Nuevo nodo
second_num_list2 = Node(2)  # Nuevo nodo
third_num_list2 = Node(3)  # Nuevo nodo
fourth_num_list2 = Node(4)  # Nuevo nodo

# Nodos en la lista2
list2.insert_end(fourth_num_list2)
list2.insert_end(second_num_list2)
list2.insert_end(first_num_list2)
list2.insert_end(third_num_list2)

print("Lista 2 :")
list2.print_list()


current_list1 = list1.head
current_list2 = list2.head

for i in range(list1.get_length()):
    while current_list1.next is not None:
        if current_list1.data > current_list1.next.data:
            aux = current_list1.next.data
            current_list1.next.data = current_list1.data
            current_list1.data = aux
            current_list1 = current_list1.next
        else:
            current_list1 = current_list1.next

print(f"Sorted? ")
list1.print_list()
