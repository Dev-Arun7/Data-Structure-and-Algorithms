# Add node at the end using loop to reach at the end
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_list:
    def __init__(self):
        self.head = None

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
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

L1 = Linked_list()
L1.append(10)
L1.append(20)
L1.append(30)
L1.print()

 