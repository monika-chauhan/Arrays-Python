# Time complexity = O(n)
# space complexity = O(1)

def OneElement(a):
    hash = {}
    for i in a:
        hash[i] = hash.get(i,0)+1

    for key in hash.keys():
        if hash[key] == 1:
            return key
    return -1

a = [1,2,3,3,1,4,2]
print(OneElement(a))