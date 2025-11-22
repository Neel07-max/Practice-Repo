import pickle
def write():
    f=open("mfile.dat",'wb')
    r=[]
    while True:
        roll=int(input("Enter Roll: "))
        name=input("Enter Name: ")
        marks=int(input("Enter marks: "))
        d=[roll,name,marks]
        r.append(d)
        choice=int(input("Enter Your Choice \n 1--> Enter Data \n 2--> Exit "))
        if choice==2:
            break
    pickle.dump(r,f)
    print("File created Successfully..")
    f.close()
def read():
    f=open("mfile.dat","rb")
    d=pickle.load(f)
    for i in d:
        print(i)
    f.close()
def search():
    f=open("mfile.dat","rb")
    d=pickle.load(f)
    roll=int(input("Enter Roll to search: "))
    flag=0
    for i in d:
        if i[0]==roll:
            print(i)
            flag=1
            break
    if flag==0:
        print("Roll Not found")
    f.close()
def maxi():
    f=open("mfile.dat","rb")
    d=pickle.load(f)
    maxm=d[0][2]
    for i in d:
        if i[2]>=maxm:
            maxm=i[2]
            z=i
    print("Max Marks Data: ",z)
    f.close()





   
#write()
#read()
#search()
#maxi()

