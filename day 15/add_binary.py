"""Add Binary
Easy
Given two binary strings a and b return their sum as a binary string. s"""


def add_binary(a: str, b: str) -> str:
    # Convert binary strings to integers, sum them, and convert back to binary
    sum_as_int = int(a, 2) + int(b, 2)
    # Convert the sum back to a binary string and remove 
    return bin(sum_as_int)[2:]


print(add_binary("1010", "1011")) 
print(add_binary("11", "1"))       

# Output 11000 
# Output 100