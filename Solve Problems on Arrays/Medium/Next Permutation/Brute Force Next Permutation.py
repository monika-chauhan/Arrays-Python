# Print all the permutation
def permute(i, a, s):
    if i == len(a):
        print(s)

    permute(i + 1, a, s + a[i])
    permute(i + 1, a, s)


def next_permutation(a):
    permute(0, a, '')


a = '123'
print(next_permutation(a))
