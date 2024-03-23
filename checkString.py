str=input("Enter a string:")
ucount=lcount=dcount=acount=0
for i in str:
    if i.isupper():
        ucount=ucount+1
    if i.islower():
        lcount+=1
    if i.isdigit():
        dcount+=1
    if i.isalpha():
        acount+=1
print(ucount,lcount,dcount,acount)