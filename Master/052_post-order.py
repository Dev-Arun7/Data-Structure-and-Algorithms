
# Definition of the Binary Search Tree (BST) class
class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        # If the root node's key is None, set the key to the new data
        if self.key is None:
            self.key = data
            return 
        # Prevent duplication in the BST
        if data == self.key:
            print("Duplicate...!")
            return
        # If the data is less than the current node's key,
        # proceed to the left subtree
        if data < self.key:
            if not self.left:
                self.left = BST(data) # If None, create a node
            else:
                self.left.insert(data) # If exist, recursion
            return
        # If the data is greater or equal, proceed to the right subtree
        else:
            if not self.right:
                self.right = BST(data) # If None, add node
            else:
                self.right.insert(data) # If exist, recursion
            return

    def postorder(self):
        if self.left:
            self.left.postorder()  # Recursively traverse the left subtree
        if self.right:
            self.right.postorder()  # Recursively traverse the right subtree
        print(self.key)  # Print the key of the current node


# Driver code
r = BST(10)
my_list = [12, 56, 2, 7, 8]
for i in my_list:
    r.insert(i)

r.postorder()

