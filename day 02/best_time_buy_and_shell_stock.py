"""Best Time to Buy and Sell Stock
You are given an array
stock on the
ith
prices
where
prices[i]
Easy
is the price of a given
day.
You want to maximize your profit by choosing a single day to buy one
stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return
Practice
0
"""


def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price if the current price is lower
        min_price = min(min_price, price)
        # Calculate the current profit and update the maximum profit
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)

    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Output: 5

prices = [7, 6, 4, 3, 1]
print(max_profit(prices))  # Output: 0
