def linearSearch(a, target):
    for i in range(len(a)):
        if a[i] == target:
            return True
    return False


a = [1, 2, 3, 4, 2, 1]
print(linearSearch(a, 1))
