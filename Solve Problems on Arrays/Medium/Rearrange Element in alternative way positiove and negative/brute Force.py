# time = O(N+N/2)
# Space = O(N) 
def rearrange(a):
    pos = []
    neg = []
    for i in range(len(a)):
        if a[i] < 0:
            neg.append(a[i])
        else:
            pos.append(a[i])

    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        a[2*i] = pos[i]
    for i in range(len(neg)):
        a[2*i+1] = neg[i]

    return a

a = [1, 2, -4, -5]
print(rearrange(a))
