userinput=input("Enter a list of elements separated by spaces:")
mylist=[int(x) for x in userinput.split()]
newmylist=[]
for i in mylist:
    if (i not in newmylist):
        newmylist.append(i)
print("List after removing duplicate:",sorted(newmylist))