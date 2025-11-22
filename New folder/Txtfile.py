def fun():
    f=open ("test.txt","r")
    while True:
        roll=int(input("Enter Roll: "))
        name=input("Enter Name: ")
        marks=int(input("Enter Marks: "))
        d=str(roll)+"\t"+name+"\t"+str("marks")+"\n"
        f.write(d)
        choice=int(input("ENter your choice 1--> ENter MOre \n 2"))        
    f.close()
fun()