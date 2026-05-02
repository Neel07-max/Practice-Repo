def user():
    count=0;
    pos_count = 0;
    neg_count = 0;
    while True:
        n=int(input("Enter any Nos: "))
        if n==0:
            break
        if n > 0:
            pos_sum += n
        else:
            neg_sum += n
    count = pos_sum + neg_sum
    print("Sum of all Nos : ", count)

user()