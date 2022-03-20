'''
PROBLEM 1 USING THE STACKS DATA STRUCTURE:

This is the Expanded problem used in the Introductory
README file for Stacks where we will push() and pop()
a list of LEGO colored blocks into an empty list, and display the
different array sizes and final OUTPUTS.

The Operations used are all O(1): stack.push(x), 
stack.pop(), and len(stack)
'''
print('OUTPUT 1')
LEGO_blocks = []

LEGO_blocks.append('blue')
LEGO_blocks.append('red')
LEGO_blocks.append('yellow')
LEGO_blocks.append('green')
LEGO_blocks.append('black')
print(LEGO_blocks)

print('=======================\n')

print('OUTPUT 2')
LEGO_blocks = []

LEGO_blocks.append('blue')
LEGO_blocks.append('red')
LEGO_blocks.append('yellow')
LEGO_blocks.pop()
LEGO_blocks.append('green')
LEGO_blocks.pop()
LEGO_blocks.append('black')
print(LEGO_blocks)
# CONTINUE WORKING ON EXAMPLES...
print('=======================\n')

