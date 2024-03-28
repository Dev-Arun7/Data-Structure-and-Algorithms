# Doubly linked list prepend
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

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node



l = Linked_List()
l.print()
l.prepend(10)
l.prepend(20)
l.prepend(30)
l.prepend(40)
l.print()