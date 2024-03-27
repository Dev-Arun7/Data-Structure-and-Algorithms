# Add a node before given node

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty...!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def prepend(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def before(self, x, data):
        if self.head is None:
            print("Linked List is empty....!")
            return

        # if x is first node we've to pepend data in first position
        if self.head.data == x: # checking x is the first node
            new_node = Node(data)
            self.head = new_node
            return

        # Finding the x by going through the loop, here checking next node is x    
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Search not found...!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    
l = Linked_List()
l.prepend(10)
l.prepend(20)
l.prepend(30)
l.prepend(40)

l.print()

print('\n')

l.before(30, 25)
l.print()