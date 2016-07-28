def answer(t, n):
    m = 123454321
    a = [0] * n + [1]
    b = a[:]
    turns = range(1, t + 1)
        for turn in turns:
            for position in range(max(1, n - turn), n):
                b[position] = (a[position -1] + a[position] + a[position+1]) % m
                a, b = b, a
    return a[1]
