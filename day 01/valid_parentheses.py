"""Valid Parentheses
Given a string'['&']'sEasy containing just the characters
'('
,
')'
,
'{'
,
'}'
,
, determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Every close bracket has a corresponding open bracket of the same type
"""




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
