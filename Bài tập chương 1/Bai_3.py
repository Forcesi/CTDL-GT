def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b , a % b)

def gcd_non_recursive(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 30
b = 20
print(f"The GCD of {a} and {b} using recursive method is: {gcd_recursive(a, b)}")
print(f"The GCD of {a} and {b} using non-recursive method is: {gcd_non_recursive(a, b)}")
