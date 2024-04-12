
# Queue using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        if self.front == None:
            return True
        else:
            return False

    # Add data to the queue to the rear side
    def EnQueue(self, data):
        new_node = Node(data)
        if self.rear == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Set current rear node's next to new_node
            self.rear = new_node # Updating the rear node with newly added node

    # Method to remove an element from front side
    def DeQueue(self):
        if self.isempty():
            return
        else:
            temp = self.front
            self.front = temp.next

            # Handles when nodes are empty
            if self.front == None:
                self.rear = None



# Drive code
q = Queue()
q.EnQueue(0)
q.EnQueue(10)
q.EnQueue(20)
q.EnQueue(30)
q.EnQueue(40)
q.EnQueue(70)
q.DeQueue()


front = q.front.data
print(front)
rear = q.rear.data
print(rear)

