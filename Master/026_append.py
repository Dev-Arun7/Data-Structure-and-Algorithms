
# Add a node at the right end of the linked list
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

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            new_node = Node(data)
            new_node.prev = n
            n.next = new_node


l = Linked_List()
l.print()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.print()
