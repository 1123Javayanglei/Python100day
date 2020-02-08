"""
求最大公约数和最小公倍数
"""


def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)


def gcd02(a, b):
    # 递归求最大公因数
    if b == 0:
        return a;
    else:
        return gcd02(b, a % b)


def lcm02(a, b):
    # (a,b)的最小公倍数= a*b // gcd(a,b)
    return a * b // gcd02(a, b)


print('%d 和 %d 的 gcd= %d' % (4, 6, gcd(4, 6)))
print('%d 和 %d 的 gcd= %d' % (4, 6, gcd02(4, 6)))
print('%d 和 %d 的 lcm= %d' % (4, 6, lcm(4, 6)))
print('%d 和 %d 的 lcm= %d' % (4, 6, lcm02(4, 6)))
