def is_valid(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False
        else:
            return False
    
    return stack == []

# Example usage:
s = "()[]{}"
print(is_valid(s))  # Output: True
