st=input("Date written in the DD-MM-YY:")
li=st.split("-")
month=["January","February","March","April","May","June","July","August","September","October","November","December"]
order=["th","st","nd","rd","th","th","th","th","th","th"]
li[1]=month[int(li[1])-1]
if abs(int(li[2])-25)>50:
    li[2]="19"+li[2]
else:
    li[2]="20"+li[2]
li[0]=li[0]+order[int(li[0][-1])]
print(li[1]+" "+li[0]+","+li[2])