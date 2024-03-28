
# Forward and backward traversal operation 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Empty...!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data}-->", end=" ")
                n = n.next

    def print_reverse(self):
        if self.head is None:
            print("Empty...!")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(f"{n.data}-->", end=" ")
                n = n.prev


l = Linked_List()
l.print()
l.print_reverse()
