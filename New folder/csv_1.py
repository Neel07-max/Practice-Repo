import csv
def write():
    with open("fun.csv","w", newline='')as f:
        fobj=csv.writer(f)
        fobj.writerow(['Roll','Name','Marks','Average'])
        while True:
            roll=int(input("Enter Roll: "))
            name=input("Enter Name: ")
            marks=int(input("Enter Marks: "))
            avg=marks/5
            d=[roll,name.upper(),marks,avg]
            fobj.writerow(d)
            choice=int(input("Enter Your Choice\n 1--> Enter More\n 2-->Exit\n Enter your choice: "))
            if choice==2:
                break
    print("File Created Successfully")

#write()  
def read():
    with open("fun.csv","r") as f:
        fobj=csv.reader(f)
        for i in fobj:
            print(i)


def search():
    with open("fun.csv","r") as f:
        fobj=csv.reader(f)
        roll=int(input("Enter roll to serch: "))
        next(fobj)  #next is used here for checking the data from next line bcz 1st line is heading
        flag=0
        for i in fobj:
            if int(i[0])==roll:
                print(i)
                flag=1
                break
        if flag==0:
            print("Roll No Not found..")
read()
search()