"""Longest Substring Without Repeating
Characters
Medium
Given a string s find the length of the longest substring without
repeating characters"""




# def longest_substring(s: str) -> int:
#     char_set = set()
#     left = 0
#     max_length = 0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_length = max(max_length, right - left + 1)

#     return max_length


# s = "abcdabcd"
# print("Length of the longest substring without repeating characters:", longest_substring(s))




def lengthOfLongestSubstring(s: str):
    char_set = set()
    left = 0
    max_length = 0
    start = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left

    longest_substring = s[start:start + max_length]
    return max_length, longest_substring


s = "abcabcbb"
length, substring = lengthOfLongestSubstring(s)
print("Length of the longest substring without repeating characters:", length)
print("Longest substring without repeating characters:", substring)
