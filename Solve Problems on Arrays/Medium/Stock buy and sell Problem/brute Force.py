# Algorithm
# Use a for loop of ‘i’ from 0 to n.
# Use another for loop of j from ‘i+1’ to n.
# If arr[j] > arr[i] , take the difference and compare  and store it in the maxPro variable.
# Return maxPro.

# Time complexity = O(n^2)

def buyStock(price):
    maxPro = 0
    profit = 0
    for i in range(len(price)):
        for j in range(i + 1, len(price)):
            if price[j] > price[i]:
                profit = price[j] - price[i]
            maxPro = max(maxPro, profit)

    return maxPro


a = [7, 1, 5, 3, 6, 4]
print(buyStock(a))
