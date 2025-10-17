def bina(num):
    if num==0:
        return "0"
    else:
        return bina(num//2)+str(num%2)
def MapToHex(num):
    if num==10:
        return "A"
    elif num==11:
        return "B"
    elif num==12:
        return "C"
    elif num==13:
        return "D"
    elif num==14:
        return "E"
    elif num==15:
        return "F"
    else:
        return str(num)
def hexa(num):
    if num==0:
        return "0"
    else:
        return hexa(num//16)+MapToHex(num%16)


num=int(input("Enter a number:"))
convert=input("Convert to Binary or Hex:")
if convert=="Binary":
    print("num in binary is",bina(num))
else:
    print("num in hex is",hexa(num))