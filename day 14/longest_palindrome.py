"""Longest Palindrome
Easy
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with 

those letters.
Letters are case sensitive, for example, "Aa" is not considered a
palindrome here"""




class Solution:
    def longest_palindrome(self,string:str) ->int:
        length = 0 
        count = {}
        for i in string:
            if(i not in count):
                count[i] = 1
                
            else:
                count[i]+=1
        for k,v in count.items():
            length+=v//2*2
            if(length %2 ==0 and v%2==1):
                length += 1
        return  length
    

solution = Solution()
print(solution.longest_palindrome("abccccdd"))  # Output: 7
print(solution.longest_palindrome("a"))         # Output: 1
print(solution.longest_palindrome("bb"))



def long_palindrome(s: str) -> int:
    odd_chars = set()
    
    for char in s:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)
    
    # If there are odd characters, we can put one of them in the center
    if len(odd_chars) > 0:
        return len(s) - len(odd_chars) + 1
    else:
        return len(s)

# Example usage:
print(long_palindrome("abccccdd"))  # Output: 7 ("dccaccd" or "dccbccd" or similar)
print(long_palindrome("Aa"))        # Output: 1 ("A" or "a")
