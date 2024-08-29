def MoveZeroToEnd(a, n):
    for i in range(len(a)):
        if a[i] == 0:
            a.remove(a[i])
            a.append(0)
    return a


a = [1, 0, 1, 0, 2, 0, 4]
print(MoveZeroToEnd(a, len(a)))


# a= [1,0,2,0,3,0,4] = > [1,2,0,0,3,0,4]
def moveZero(a):
    temp =[]
    for i in a:
        if i != 0:
            temp.append(i)
    for i in range(len(temp)):
        a[i] = temp[i]

    for i in range(len(temp),len(a)):
        a[i] = 0
    return a

a = [1,0,2,0,3,0,4]
print(moveZero(a))




