n=int(input("Input an integer: "))
h=0;t=n
flag=True
while h<=t and flag:
    m=(h+t)//2
    if m**2<n:
        h=m+1
    elif m**2>n:
        t=m-1
    else:
        flag=False
if flag:
    print(False)
else:
    print(True)