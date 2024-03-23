mylist=eval(input("Enter the elements of the list:"))
sum=0
for i in range(0,len(mylist),2):
    sum=sum+mylist[i]
print("The sum of alternate numbers=",sum)