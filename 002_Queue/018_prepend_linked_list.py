
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print(" Linked List is empty...!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def prepend(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


L1 = Linked_List()
L1.prepend(10)
L1.prepend(20)
L1.prepend(30)
L1.print()