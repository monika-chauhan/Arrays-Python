# Time complexity = O(n)
# space complexity = O(n) because we are using Set 
def removeDuplicate(a):
    s = set()
    for i in range(len(a)):
        s.add(a[i])
    return list(s)
a = [1,2,3,1,3,4,5]
print(removeDuplicate(a))