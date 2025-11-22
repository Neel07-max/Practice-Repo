'''def fun():
    a= int(input("enter no."))
    b= int(input("enter no."))
    c=a+b
    print("Sum:",c)
    if c%2==0:
        print("True")
    else:
        print("False")
fun()
'''
'''
#Sum of list
def sum():
    a=[]
    s=int(input("Enter No."))
    for i in range (s):
        v=int(input("Enter Value:"))
        a.append(v)
    print("The list is :",a)
    sum=0
    for i in range (s):
        sum=sum+a[i]
    print("Sum of list",sum)
sum()
'''

#calling the function
'''
def fun(a,b):
    c=a-b
    print("Substraction: ",c)

a=int(input("Enter 1st no: "))
b=int(input("Enter 2nd no: "))
 
fun(a,b)
'''
'''
def prime(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        print("Prime")
    else:
        print("Not prime")

a=int(input("Enter any No."))
print(a)

prime(a)
'''

