def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a + b, c + d)

    return ac * 10**(2*m) + (ab_cd - ac - bd) * 10**m + bd