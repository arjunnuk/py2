li=[]
n=int(input("enter the value of n"))
for i in range(0,n):
    print("enter the element",i+1)
    x=int(input())
    li.append(x)
print(li)
psum=0
nsum=0
for i in li:
    if(i>0):
        psum=psum+i
    else:
        nsum=nsum+i
print("the sum positive numbers is",psum)
print("the sm negative numbers is",nsum)
print("arjunuk")
