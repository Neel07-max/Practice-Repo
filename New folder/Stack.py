#                                              !!!  Stack Program !!!
def push(a,value):
    a.append(value)
    print("Element Pushed")

def pop(a):
    x=a.pop()
    print("Poped element: ",x)

def peek(a):
    print("PeekElement: ",a[-1])

def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])
#__main__
a=[]
while True:
    choice=int(input("Enter Your Choice \n 1--> Enter Data \n 2-->Pop data \n 3-->Peek Elements \n 4--> Display All \n 5--> Exit "))
    if choice==1:
        value=int(input("Enter No: "))
        push(a,value) 
    elif choice==2:
        if len(a)==2:
            print("List is Empty")
        else:
            pop(a)
    elif choice==3:
        if len(a)==0:
            print("Stack Is UnderrFlow")
        else:
            peek(a)
    elif choice==4:
        if len(a)==0:
            print("Stack Is Empty")
        else:
            display(a,end=" ")
    elif choice==5:
        break
    else:
        print("Choice is Out of Range..!!")