x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
if x>y:
    small=y
else:
    small=x
for i in range(1,small+1):
    if((x%i==0)and(y%i==0)):
        gcd=i
print("The Gcd=",gcd)