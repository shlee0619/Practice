import time

def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


start = time.time()
print(factorial_iterative(5))
end = time.time()
print(end - start)

start = time.time()
print(factorial_recursive(5))
end = time.time()
print(end - start)
