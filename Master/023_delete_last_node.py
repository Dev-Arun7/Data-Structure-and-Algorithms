# Deleting the last node

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        n = self.head
        if n is None:
            print("Empty...!")
        else:
            while n is not None:
                print(n.data, "-->", end=" ")
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

    def delete(self):
        if self.head is None:
            print("Empty")
        elif self.head.ref is None: #This is used to the case where only one node is present on the Linked list
            self.head = None
        else:  # Rest of the time this case will work
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None


l = Linked_List()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.print()
print("\n")


l.delete()
l.print()
