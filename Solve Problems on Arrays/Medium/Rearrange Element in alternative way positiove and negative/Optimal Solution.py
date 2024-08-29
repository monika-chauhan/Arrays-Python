def rearrange(a):
    posIndex = 0
    negIndex = 1
    ans = [0]*len(a)
    for i in range(len(a)):
        if a[i] < 0:
            ans[negIndex] = a[i]
            negIndex += 2
        else:
            ans[posIndex] = a[i]
            posIndex += 2
    return ans

a = [1,2,-4,-5]
print(rearrange(a))