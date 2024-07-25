"""Ransom Note
Easy
Given two strings ransomNote and magazine , return true if ransomNote
can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote"""

from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    # Count frequencies of each character in magazine
    magazine_count = Counter(magazine)
    
    for char in ransom_note:
        if magazine_count[char] > 0:
            magazine_count[char] -= 1
        else:
            return False
    
    return True
ransom_note = "aabb"
magazine =   "aabbc"
print(can_construct(ransom_note, magazine))  # Output: True

ransom_note = "aa"
magazine = "aab"
print(can_construct(ransom_note, magazine))  # Output: True

ransom_note = "aaa"
magazine = "aab"
print(can_construct(ransom_note, magazine))  # Output: False
