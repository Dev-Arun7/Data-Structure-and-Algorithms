
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

    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty!")
            return self

        if data < self.key:
            if self.left: 
                self.left = self.left.delete(data, curr)
            else:
                print("No match found!")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data, curr)
            else:
                print("No match found!")
        else:
            if self.left is None:
                temp = self.right
                if data == curr:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                self = None
                return temp
            elif self.right is None: 
                temp = self.left
                if data == curr:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right
                    temp = None
                    return
                self = None
                return temp
            else:
                # Node with two children: Get the inorder successor
                # (smallest in the right subtree)
                temp = self.right
                while temp.left:
                    temp = temp.left
                # Copy the inorder successor's content to this node
                self.key = temp.key
                # Delete the inorder successor
                self.right = self.right.delete(temp.key, curr)
        return self


    def inorder(self): 
        if self.left:
            self.left.inorder()  # Recursively traverse the left subtree
        print(self.key, end = ", ")  # Print the key of the current node
        if self.right:
            self.right.inorder()  # Recursively traverse the right subtree
 

####----------Driver code---------###

# Function to check number of nodes on the BST
def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

r = BST(10)
my_list = [2, 6, 12, 45]

for i in my_list:
    r.insert(i)

r.inorder()

# Printing the count
print("\n Count: ", count(r))

if count(r) > 1:
    r.delete(10, r.key)
else:
    print("Can't perform deletion")

print("\n")
r.inorder()

