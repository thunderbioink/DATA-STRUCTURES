"""
PROBLEM#1:

The purpose for this Binary Tree exercise is for you to be able to see
how a Binary Tree can be built.

It is a very similar way to how we made a Linked List. The display of the

OUTPUT is different.

Binary Trees are complex, but understanding the creation of a root Node, the
parent Node, and the Child Nodes, can aid in better using this Data Structure.

You will have to observe this code, and use it to help you solve Problem #2.


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
    pass

# DISPLAY NODE VALUES IN BINARY TREE:
    def display_binary_tree(self):
        # You need 2 if statements:
        # for self.right
        # for self.left
        pass    

#BUILD BINARY TREE INPUTING NODE DATA BELOW:
print("\n==============\n")
print("\n BINARY TREE: CHILD to PARENT NODE DISPLAY: \n")
# root = Binary_tree(20)
# root.add_node(10)
# root.add_node(15)
# root.add_node(5)
# root.display_binary_tree()
print("\n==============\n")

"""
EXPECTED OUTPUT PROBLEM #1:

==============


 BINARY TREE: CHILD to PARENT NODE DISPLAY: 

==============

"""