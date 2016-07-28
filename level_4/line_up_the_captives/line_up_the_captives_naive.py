from itertools import permutations

def answer(x, y, n):
    perms = list(permutations(range(0, n)))
    count = 0
    for perm in perms:
        max = perm[0]
        from_left = 1
        for item in perm:
            if item > max:
                max = item
                from_left += 1
        from_right = 1
        perm_right = list(reversed(perm))
        max = perm_right[0]
        for item in perm_right:
            if item > max:
                max = item
                from_right += 1
        if from_left == x and from_right == y:
            count += 1
    return(count)
