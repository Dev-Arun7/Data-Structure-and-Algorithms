class Node:
    def __init__(self, data):
        self.ref = None
        self.data = data
    
class Linked_List:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref

            n.ref = new_node

l1 = Linked_List()
l1.prepend(1)
l1.prepend(10)
l1.prepend(100)
l1.prepend(1000)
l1.print_ll()