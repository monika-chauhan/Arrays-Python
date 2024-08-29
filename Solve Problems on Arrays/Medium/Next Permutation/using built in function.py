from itertools import permutations


def next_permutation(a):
    array = []
    for i in permutations(sorted(a)):
        array.append(list(i))
        
    for i in range(len(array)):
        if array[i] == a:
            if array[i] == array[-1]:
                return array[0]
            else:
                return array[i + 1]


a = [1, 3, 2]
print(next_permutation(a))
