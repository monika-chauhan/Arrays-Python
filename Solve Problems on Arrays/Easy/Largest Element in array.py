def LargestEle(a):
    mini = a[0]
    for i in range(len(a)):
        if a[i] > mini:
            mini = a[i]
    return mini

a = [3,4,1,5,7,9]
print(LargestEle(a))