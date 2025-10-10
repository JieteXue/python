a=int(input("The first integer:"))
b=int(input("The second integer:"))
c=int(input("The third integer:"))
flag=False
if a>b:
    m=a
else:
    m=b
if m>c:
    print(m)
    if a==b:
        flag=True
else:
    print(c)
    if m==c:
        flag=True
if flag:
    print("Tie")

w=float(input("Your weight in kg:"))
h=float(input("Your height in m:"))
BMI=w/(h)**2
print("Your BMI is",round(BMI,2))
if BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Fit")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")