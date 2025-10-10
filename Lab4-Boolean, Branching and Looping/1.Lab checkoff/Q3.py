n=int(input("Enter number of rows in pyramid:"))
for i in range(0,int(n)):
    print((n-i)*" "+(2*i+1)*"#"+"\r" )