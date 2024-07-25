"""# 3Sum
# Medium
# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j , i != k and j != k ,
# and nums[i] + nums[j] + nums[k] == 0
# Notice that the solution set must not contain duplicate triplets"""



def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        target = -nums[i]
        seen = {}
        
        for j in range(i + 1, n):
            complement = target - nums[j]
            if complement in seen:
                triplet = [nums[i], complement, nums[j]]
                if triplet not in result:
                    result.append(triplet)
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
            seen[nums[j]] = j
        
    return result

# Example usage:
print(three_sum([-1, 0, 1, 2, -1, -4]))
