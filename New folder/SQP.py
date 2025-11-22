'''
def Puzzle(W,N):
    NW=""
    c=1
    for ch in W:
        if c!=N:
            NW+=ch
            c+=1
        else:
            NW+="_"
            c=1
    return NW
W=input("Enter any Word: ")
N=int(input("Enter any No.: "))
print(Puzzle(W,N))

def swap_first_last(tup):
    if len(tup)<2:
        return tup
    new_tup=(tup[-1],) + tup[1:-1] + (tup[0],)
    return new_tup
result=swap_first_last((1,2,3,4))
print("Swappwed Tupple: ", result)'
'''


x=("12546987")
print(len(x))