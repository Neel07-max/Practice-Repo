# n=3452
# while n>0:
#     r=n%10
#     print(r,end="")
#     n=n//10
# print()

def palindrome(n):
    rev = 0
    temp = n
    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    return rev == temp

print(palindrome(545))  
print(palindrome(123))
