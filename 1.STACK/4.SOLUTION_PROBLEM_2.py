
"""
SOLUTION TO PROBLEM #2:

"""
# Create empty list to append(push) LEGO blocks to:
LEGO_BLOCKS = []

# LEGO BLOCK 1 : BLUE 
LEGO1 = ("BLUE")
LEGO_BLOCKS.append(LEGO1)

# LEGO BLOCK2: RED -------> Remove without deleting the code.
LEGO2 = ("RED")
LEGO_BLOCKS.append(LEGO2)
LEGO_BLOCKS.pop()

# LEGO BLOCK 3: YELLOW
LEGO3 = ("YELLOW")
LEGO_BLOCKS.append(LEGO3)

# LEGO BLOCK 4: GREEN
LEGO4 = ("GREEN")
LEGO_BLOCKS.append(LEGO4)

# LEGO BLOCK 5: BLACK ----> Remove without deleting the code.
LEGO5 = (("BLACK"))
LEGO_BLOCKS.append(LEGO5)
LEGO_BLOCKS.pop()

# LEGO BLOCK 6: ORANGE
LEGO6 = ("ORANGE")
LEGO_BLOCKS.append(LEGO6)

print('=======================\n')
print("OUTPUT PROBLEM #2: \n")

for x in LEGO_BLOCKS:
    #print colors
    print("- LEGO BLOCK : ", x, "\n")
     
print("\n")

# Print Length of List/Stack of LEGO Blocks

len_LEGO_blocks = len(LEGO_BLOCKS)
print(f"\nTotal amount of LEGO Blocks = '{len_LEGO_blocks}'.\n")


