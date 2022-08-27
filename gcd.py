#GCD using recursion
a/b a= dividend,b=divisor
def gcd(dividend, divisor):
    if (dividend % divisor) == 0:
        return divisor
    return gcd(divisor, (dividend % divisor))


def lcm(a, b):
    return int(a*b/gcd(a, b))


print(gcd(4, 12))
print(lcm(4, 12))
