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
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            n = self.head
            new_node = Node(data)
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def delete_by_value(self, x):
        n = self.head
        if self.head is None:
            print("Empty....!")
        elif x == n.data:    # Checking given value is in first node.
            self.head = n.ref
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    n.ref = n.ref.ref
                    return
                n = n.ref
                

            print("No match found...!")  


l = Linked_List()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.print()

print("\nDeleting....")

l.delete_by_value(30)
l.print()
