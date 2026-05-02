def fibo(n: int) -> int:
    
    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2) + fibo(n-3)

n = int(input("Enter a number: "))
print(fibo(n))