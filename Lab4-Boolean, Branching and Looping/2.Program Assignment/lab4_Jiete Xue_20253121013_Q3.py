n=int(input("Enter a integer:"))
i=2
while True:
    if n%i==0:
        print(str(n)+" is not a prime number")
        break
    i+=1
    if i>n**0.5:
        print(str(n)+" is a prime number")
        break
