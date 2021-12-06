def BinPow(a, n, f):
    if n == 1:
        return a
    elif n % 2 == 1:
        return f(BinPow(a, n - 1, f), a)
    else:
        return BinPow(f(a, a), n // 2, f)
