'''
PROBLEM 1 USING THE STACKS DATA STRUCTURE:

This is the Expanded problem used in the Introductory
README file for Stacks where we will push(x) and pop(x)
a list of LEGO colored blocks into an empty list. 
The list size will be displayed with final OUTPUTS.

The Operations used are all O(1): stack.push(x), 
stack.pop(), and len(stack).


'''
print('\nLEGO BLOCK LIST #1:\n')
LEGO_blocks1 = []

LEGO_blocks1.append('blue')
LEGO_blocks1.append('red')
LEGO_blocks1.append('yellow')
LEGO_blocks1.append('green')
LEGO_blocks1.append('black')
print(LEGO_blocks1)
print("\n")
len_LG1 = len(LEGO_blocks1)
print(f"LENGTH OF LEGO BLOCKS LIST #1: {len_LG1}")

print('=======================\n')

print('\nLEGO BLOCK LIST #2:\n')
LEGO_blocks2 = []

LEGO_blocks2.append('blue')
LEGO_blocks2.append('red')
LEGO_blocks2.append('yellow')
LEGO_blocks2.pop()
LEGO_blocks2.append('green')
LEGO_blocks2.pop()
LEGO_blocks2.append('black')
print(LEGO_blocks2)
print("\n")
len_LG2 = len(LEGO_blocks2)
print(f"LENGTH OF LEGO BLOCKS LIST #2: {len_LG2}")

print("""
        
            Notice that the LIFO principle applies here by seeing that
            Last In is the First Out:
            - Blue is First In, hence it's Last Out.
            - Red is Second In, hence it is neither First or Last Out.
            - Yellow is at this stage of the code, Last In, and we call pop()
            and it is now the First Out.
            - Same with green. It becomes the Last In, and we call pop()
            and it is now the First Out.
            - Black is Last In, hence, if we added pop() it would become First Out.
            
""")
print('=======================\n')

"""
DESIRED OUTPUT FOR LEGO BLOCKS LIST #1:
LEGO BLOCK LIST #1:

['blue', 'red', 'yellow', 'green', 'black']


LENGTH OF LEGO BLOCKS LIST #1: 5
=======================
DESIRED OUTPUT FOR LEGO BLOCK LIST #2:


['blue', 'red', 'black']


LENGTH OF LEGO BLOCKS LIST #2: 3
=======================

"""
