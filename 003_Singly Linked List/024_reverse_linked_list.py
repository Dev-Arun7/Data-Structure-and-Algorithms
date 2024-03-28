# Reverse a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty...!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data}-->", end=" ")
                n = n.ref

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.head = prev
         

L1 = Linked_List()
L1.append(10)
L1.append(20)
L1.append(30)
L1.print()
print("\n")

L1.reverse()
L1.print()
