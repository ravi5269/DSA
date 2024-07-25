"""Suppose you have n versions [1, 2, ..., n] and you want to find out
the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether
version is bad. Implement a function to find the first bad version"""

def bad_version(version: int) -> bool:
    # return version >= 6
    pass

def first_bad_version(n: int) -> int:
    left, right = 1, n
    
    while left <= right:
        mid = (left + right) // 2
        if bad_version(mid):
            if mid == 1 or not bad_version(mid - 1):
                return mid
            else:
                right = mid - 1
        else:
            left = mid + 1
    
    return -1  # No bad version found


n = 10  # Number of versions
first_bad = first_bad_version(n)
if first_bad != -1:
    print(f"The first bad version is: {first_bad}")
else:
    print("No bad versions found.")
