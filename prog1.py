x,y,z= input("Enter three numbers")
x,y,z=int(x),int(y),int(z)
min=mid=max=None
if x<y and x<z:
    if y>z:
        min,mid,max=x,z,y
    else:
        min,mid,max=x,y,z
if y<x and y<z:
    if x>y:
        min,mid,max=y,z,x
    else:
        min,mid,max=y,x,z
if z<x and z<y:
    if x>y:
        min,mid,max=z,y,x
    else:
        min,mid,max=z,x,y  
print(min,mid,max)  
