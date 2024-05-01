
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
    
    #  Method to find Min in BST
    def min_node(self):
        current = self
        while current.left:
            current = current.left
        return current.key

    # Method to find max value
    def max_node(self):
        current = self
        while current.right:
            current = current.right
        return current.key


    def inorder(self): 
        if self.left:
            self.left.inorder()  # Recursively traverse the left subtree
        print(self.key, end = ", ")  # Print the key of the current node
        if self.right:
            self.right.inorder()  # Recursively traverse the right subtree
 

####----------Driver code---------###
r = BST(10)
my_list = [2, 6, 12, 45]

for i in my_list:
    r.insert(i)

r.inorder()

min_node = r.min_node()
print(min_node)
print(r.min_node())


print("\n")
r.inorder()

