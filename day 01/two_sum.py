def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # If no solution is found

# Example usage:
nums = [2,7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1] (indices of 2 and 7)
