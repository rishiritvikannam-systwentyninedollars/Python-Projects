def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

nterms = 10

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibonacci(i))