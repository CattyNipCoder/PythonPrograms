mylist=[]
n=int(input("How many numbers:"))
for i in range(0,n):
    x=int(input("Enter the element:"))
    mylist.append(x)
elist=[]
olist=[]
sum=0
count=0
for i in mylist:
    if(i%2==0):
        elist.append(i)
    else:
        olist.append(i)
    sum=sum+i
    count=count+1
print("Even list=",sorted(elist))
print("Odd list=", sorted(olist))
print("Sum of elements=",sum)
print("No. of elements=",count)