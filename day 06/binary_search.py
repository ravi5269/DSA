"""Binary Search
Easy
Given an array of integers nums which is sorted in ascending order, and
an integer target , write a function to search target in nums . If target
exists, then return its index. Otherwise, return -1 .
You must write an algorithm with 0(log n) runtime complexity"""

def binary_search(array, target): 
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return -1

nums = [10,20,30,40,50]
target = 40
print(binary_search(nums, target)) 


    

    
