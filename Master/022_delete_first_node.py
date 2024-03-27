# Deleting the first node if present

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Empty...!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data} --->", end= " " )
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

    def delete_begin(self):
        if self.head is None:
            print("Empty....!")
        else:
            self.head = self.head.ref


L1 = Linked_List()
L1.append(10)
L1.append(20)
L1.append(30)
L1.print()
print("\n")

 
L1.delete_begin() # Calling delete
L1.print()
