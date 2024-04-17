""" Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull()
and an additional operation getMin() which should return minimum element from the SpecialStack.
All these operations of SpecialStack must have a time and space complexity of O(1). """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to implement stack using linked list
class Stack:
    def __init__(self):
        self.head = None
        self.minimum = None

    # Checks if stack is empty
    def isempty(self):
        return self.head == None

    # Method to add data to the stack
    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.minimum = data
        elif data < self.minimum:
            new_data = 2 * data - self.minimum
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            self.minimum = data
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head

    # Remove element that is the current head (start of the stack)
    def pop(self):
        if self.isempty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            if popped_node.data < self.minimum:
                self.minimum = 2 * self.minimum - popped_node.data
            return popped_node.data

    # Returns the head node data
    def peek(self):
        return self.head.data if self.head else None

    # Returns the minimum element in the stack
    def getMin(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.minimum

    # Prints out the stack
    def display(self):
        if self.isempty():
            print("Stack Underflow")
        else:
            current = self.head
            while current:
                print(f"{current.data}-->", end=" ")
                current = current.next
            print()

# Driver code
MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(7)  # New minimum
MyStack.push(5)   # New minimum

# Display stack elements
MyStack.display()

# Print top element of stack
print("Top element is ", MyStack.peek())

# Print minimum element of stack
print("Minimum element is ", MyStack.getMin())

# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display stack elements
MyStack.display()

# Print top element of stack
print("Top element is ", MyStack.peek())

# Print minimum element of stack
print("Minimum element is ", MyStack.getMin())
