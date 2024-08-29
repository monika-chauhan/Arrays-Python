## time complexity = O(n^2)
def checkSorted(a):
    for i in range(len(a)):  # --- O(n)
        for j in range(i + 1, len(a) - 1):  # --- O(n)
            if a[i] > a[j]:
                return False
    return True


a = [1, 2, 3, 4, 5]
print(checkSorted(a))
b = [2, 3, 41, 5, 6]
print(checkSorted(b))
