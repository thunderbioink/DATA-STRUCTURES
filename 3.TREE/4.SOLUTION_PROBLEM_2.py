"""
FULL BINARY TREE SOLUTION FOR PROBLEM#2:



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
    pass#remove this line once problem is solved.

# DISPLAY NODE VALUES IN BINARY TREE:
    def display_binary_tree(self):
        if self.left_child:
            self.left_child.display_binary_tree()
        print( self.data),
        if self.right_child:
            self.right_child.display_binary_tree()
    pass#remove this line once problem is solved.
    
            

#BUILD BINARY TREE INPUTING NODE DATA BELOW:
print("\n==============\n")
print("\n BINARY TREE: CHILD to PARENT NODE DISPLAY: \n")
# Uncomment next lines of code once solution reached:
# root = Binary_tree(20)
# root.add_node(10)
# root.add_node(15)
# root.add_node(5)
# root.display_binary_tree()
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