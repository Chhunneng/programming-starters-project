def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

fibonacci = [fib(i) for i in range(10)]
print("Os 10 primeiros números de Fibonacci são:", fibonacci)