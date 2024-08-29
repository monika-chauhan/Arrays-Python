# Create a variable maxPro and store 0 initially.
# Create a variable minPrice and store some larger value(ex: MAX_VALUE) value initially.
# Run a for loop from 0 to n.
# Update the minPrice if it is greater than the current element of the array
# Take the difference of the minPrice with the current element of the array and compare and maintain it in maxPro.
# Return the maxPro.

def buyStock(price):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(price)):
        minPrice = min(minPrice, price[i])
        maxPro = max(maxPro, price[i] - minPrice)
    return maxPro


a = [7, 6, 4, 3, 1]
b = [7, 1, 5, 3, 6, 4]
print(buyStock(b))
