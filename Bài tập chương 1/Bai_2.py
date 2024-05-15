def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)  

def Neper(n):
  e = 0
  for k in range(n + 1):
      e += factorial(k)
  return e

n = 4
print("Tổng của a0 + a1 + ... + an với n =", n, "là:", Neper(n))  
