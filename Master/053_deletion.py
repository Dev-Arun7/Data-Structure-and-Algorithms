
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

    def delete(self, data):
        if self.key is None:
            print("Tree is empty!")
            return self

        if data < self.key:
            if self.left: 
                self.left = self.left.delete(data)
            else:
                print("No match found!")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("No match found!")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None: 
                temp = self.left
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
                self.right = self.right.delete(temp.key)
        return self


    def inorder(self): 
        if self.left:
            self.left.inorder()  # Recursively traverse the left subtree
        print(self.key, end = ", ")  # Print the key of the current node
        if self.right:
            self.right.inorder()  # Recursively traverse the right subtree
 

# Driver code
r = BST(10)
my_list = [12, 56, 2, 7, 8]
for i in my_list:
    r.insert(i)

r.inorder()

print("\n")
r.delete(56)
r.inorder()
