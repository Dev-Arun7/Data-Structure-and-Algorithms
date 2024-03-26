# Append at the right side without using while loop

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None  

    def print(self):
        if self.head is None:
            print("Linked list is empty...!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.ref = new_node  # Update the current tail's reference to point to the new node
            self.tail = new_node  # Update the tail reference to the new node

L1 = Linked_list()
L1.append(10)
L1.append(20)
L1.append(30)
L1.append(40)
L1.print()
