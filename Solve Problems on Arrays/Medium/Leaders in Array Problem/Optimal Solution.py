# Time = O(n)
# Space = O(n)

def leader(a):
    ans = []
    n = len(a)

    # Last element of an aay is always a leader,
    # push into ans aay.
    max_elem = a[n - 1]
    ans.append(a[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if a[i] > max_elem:
            ans.append(a[i])
            max_elem = a[i]

    for i in range(len(ans)-1,-1,-1):
        print(ans[i],end=' ')


a = [10, 22, 12, 3, 0, 6]
leader(a)
