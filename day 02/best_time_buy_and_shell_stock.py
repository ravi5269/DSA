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
