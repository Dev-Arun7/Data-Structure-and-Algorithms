
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Empty...!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} --->", end=" ")
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

    # This method is used to insert a node after x
    def after(self, data, x):
        n = self.head
        while n.ref is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Search not found...!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


l = Linked_List()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.print_ll()


# Here adding 25 after the element 20
l.after(25, 20)
print("\n") # Adding a new line
l.print_ll()


