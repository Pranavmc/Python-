a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>=b and a>=c):
    print("a is largest:",a)
elif(b>=c):
    print("b is largest:",b)
else:
    print("c is largest:",c)