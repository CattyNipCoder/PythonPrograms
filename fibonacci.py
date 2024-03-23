nterms=int(input("Enter the number of terms:"))
n1,n2=0,1
count=0
print("Fibonacci Series:")
while count<nterms:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1