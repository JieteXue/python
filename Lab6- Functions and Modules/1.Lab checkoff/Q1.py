def argmax(tuple):
    max=tuple[0]
    t=0
    for i in range(len(tuple)):
        if tuple[i]>max:
            max=tuple[i]
            t=i
    return max,t
print (argmax((1,2,3,4,5)))
def mol(*args):
    m=1
    for i in range(len(args)):
        m=m*float(args[i])
    return m
print(mol(1,2,3,1.5,-5))

def Qleap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def leap_year():
    year1=int(input("Enter start year:"))
    year2=int(input("Enter end year:"))
    year=()
    for i in range(year1,year2+1):
        if Qleap_year(i):
            year=year+(i,)
    return year
print(leap_year())