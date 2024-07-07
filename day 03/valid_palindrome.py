def is_valid_palindrome(s):
    filtered_string = ""

    for char in s:
        if char.isalnum():
            filtered_string += char.lower()
            
    return filtered_string == filtered_string[::-1]

# Example usage:
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(is_valid_palindrome(s1))  # Output: True
print(is_valid_palindrome(s2))  # Output: False
