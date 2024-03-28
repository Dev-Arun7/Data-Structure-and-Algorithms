
# Add a node after a node in doubly linked list
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
            print("Empty..!")
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

    def add_after(self, x, data):
        if self.head is None:
            print("Empty...!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    new_node = Node(data)
                    new_node.next = n.next
                    new_node.prev = n
                    if n.next is not None: # checking this is the last node.
                        n.next.prev = new_node
                    n.next = new_node
                    return
                n = n.next
            print("No match found")


l = Linked_List()
# l.print_reverse()
print('\n')

l.append(10)
l.append(20)
l.append(30)
l.print()
print('\n')

l.add_after(20, 25)
l.print()


 