def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    z0 = karatsuba(b, d)
    z1 = karatsuba(a + b, c + d)
    z2 = karatsuba(a, c)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("Resultado:", karatsuba(x, y))
