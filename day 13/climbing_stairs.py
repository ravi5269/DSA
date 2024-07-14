"""Climbing Stairs
Easy
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top"""



def climb_stairs(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    
    # Initialize variables to store number of ways to reach current and previous steps
    prev1 = 1  # Represents number of ways to reach 1 step back
    prev2 = 1  # Represents number of ways to reach 2 steps back
    
    # Iterate from step 2 to n
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


print(climb_stairs(2))  # Output: 2
print(climb_stairs(3))  # Output: 3
print(climb_stairs(4))  # Output: 5
