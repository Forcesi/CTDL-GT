# Phương thức Fibonacci đệ quy
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Phương thức Fibonacci không đệ quy
def fibonacci_non_recursive(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        temp = a + b
        a = b
        b = temp
    return b 

n = 6
print(f"Số Fibonacci tại vị trí {n} đệ quy: {fibonacci_recursive(n)}")
print(f"Số Fibonacci tại vị trí {n} không đệ quy: {fibonacci_non_recursive(n)}")