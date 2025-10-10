word=input("Enter the verb:")
word0=word
if word=="have":
    print("has")
else:
    dic={}
    li=["o","s","h","z","x"]
    for i in range(5):
        dic[li[i]]=li[i]+"es"
    for i in range(5):
        word=word.replace(li[i],dic[li[i]])
    if word[-1]=="y":
        word=word[:-1]+"ies"
    if word==word0:
        print(word+"s")
    else:
        print(word)