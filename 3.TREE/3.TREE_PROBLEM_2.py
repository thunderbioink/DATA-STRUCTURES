"""
PROBLEM#2:

The purpose for this Binary Tree exercise is for you to be able to build 
the method that displays your Binary Tree Data:

You will have clues provided and you can use Problem#1 to solve display_binary_tree()
method.

USE SOLUTION TO COMAPRE YOUR WITH SOLUTION.
GOOD LUCK!


"""

class Binary_tree:
    # INITIATE BINARY TREE DATA:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data

    def add_node(self, data):
        # CHECK THAT ADDED NODE IS NOT EQUAL TO PARENT NODE:
        if self.data:
            if data < self.data:
                if self.left_child is None:
                    self.left_child = Binary_tree(data)
                else:
                    self.left_child.add_node(data)
            elif data > self.data:
                if self.right_child is None:
                    self.right_child = Binary_tree(data)
                else:
                    self.right_child.add_node(data)
        else:
            self.data = data

# DISPLAY NODE VALUES IN BINARY TREE:
    def display_binary_tree(self):
        # You need 2 if statements:
        # for self.right
        # for self.left
        pass    

#BUILD BINARY TREE INPUTING NODE DATA BELOW:
print("\n==============\n")
print("\n BINARY TREE: CHILD to PARENT NODE DISPLAY: \n")
root = Binary_tree(20)
root.add_node(10)
root.add_node(15)
root.add_node(5)
root.display_binary_tree()
print("\n==============\n")

"""
EXPECTED OUTPUT PROBLEM #2:

==============


 BINARY TREE: CHILD to PARENT NODE DISPLAY: 

5
10
15
20

==============

"""