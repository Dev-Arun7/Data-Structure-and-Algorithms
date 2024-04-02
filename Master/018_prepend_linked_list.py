
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



nums = [ 11, 22, 55, 66, 77]
L1 = Linked_List()


for i in nums:
    L1.prepend(i)
L1.print()