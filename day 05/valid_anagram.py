"""Valid Anagram
Easy
Given two strings s and t , return true if t is an anagram of s , and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once."""

from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    # Count the frequency of each character in both strings and compare
    return Counter(s) == Counter(t)

s = "ravi"
t = "ivar"
print(is_anagram(s, t))  # Output: True

s = "rat"
t = "car"
print(is_anagram(s, t))  # Output: False
