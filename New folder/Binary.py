import pickle
def write():
    f=open("MyBinary.dat","wb")
    record=[]
    while True:
        roll=int(input("Enter Roll No.: "))
        name=input("Enter name: ")
        marks=int(input("Enter Marks: "))
        d=[roll,name,marks]
        record.append(d)
        choice=int(input("Enter 1 to Add \n Enter 2 Break \n Enter 3 to Display list"))
        if choice==2:
            break
        elif choice==3:
            print(record)
    pickle.dump(record,f)
    print("File Created Successfully")
    f.close()

def read():
    f=open("MyBinary.dat","rb")
    data=pickle.load(f)
    for i in data:
        print(i)
    f.close()
#write()
#read()
