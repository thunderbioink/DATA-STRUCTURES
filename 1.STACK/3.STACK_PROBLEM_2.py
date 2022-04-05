
"""
You will have to solve the following problem
by finding a way to remove the LEGO Blocks 
BLACK & RED so we can only see the LEGO Blocks
BLUE, RED,YELLOW, GREEN, & BLACK.

Current view:

- LEGO BLOCK :  BLUE

- LEGO BLOCK :  RED

- LEGO BLOCK :  YELLOW

- LEGO BLOCK :  GREEN

- LEGO BLOCK :  BLUE

==============================

Desired view: 

- LEGO BLOCK :  BLUE

- LEGO BLOCK :  YELLOW

- LEGO BLOCK :  GREEN

- LEGO BLOCK : ORANGE

Total amount of LEGO Blocks = '4'.

===============================

The last challenge is to print out the length of the
LEGO BLock LISTS: should be '4'

You should be able to solve this using Problem 1 and
the hints provided.


"""
# Create empty list to append(push) LEGO blocks to:
LEGO_BLOCKS = []

# LEGO BLOCK 1 : BLUE 
LEGO1 = ("BLUE")
LEGO_BLOCKS.append(LEGO1)

# LEGO BLOCK2: RED -------> Remove without deleting the code.
LEGO2 = ("RED")
LEGO_BLOCKS.append(LEGO2)


# LEGO BLOCK 3: 
LEGO3 = ("YELLOW")
LEGO_BLOCKS.append(LEGO3)


# LEGO BLOCK 4:
LEGO4 = ("GREEN")
LEGO_BLOCKS.append(LEGO4)

# LEGO BLOCK 5: BLACK ----> Remove without deleting the code.
LEGO5 = (("BLACK"))
LEGO_BLOCKS.append(LEGO5)

# LEGO BLOCK 6: ORANGE ---> Add LEGO here

print('=======================\n')
print("OUTPUT PROBLEM #2:")

for x in LEGO_BLOCKS:
    #print colors
    print("- LEGO BLOCK : ", x, "\n")
     
print("\n")

# Print Length of List/Stack of LEGO Blocks

# HINT: you only need one new variable to hold the length of your LEGO_BLOCKS list. 
#  You only need one more print statement to print out the length of your list.

# Variable here
# print statement here

