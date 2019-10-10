def stockmax(a):

    c = 0
    n = len(a)

    profit = 0
    for i in range(n-1, -1, -1):
        if c < a[i]:
            c = a[i]
        profit = profit + c-a[i]
    return profit