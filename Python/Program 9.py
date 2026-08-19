# WAP to find the greatest Number entered by the User.

a = float(input("Enter 1st Number : "))
b = float(input("Enter 2nd Number : "))
c = float(input("Enter 3rd Number : "))
d = float(input("Enter 4th Number : "))

if(a>b and a>c and a>d):
    print("a is the greatest number")
elif(b>a and b>c and b>d):
    print("b is the greatest number")
elif(c>a and c>b and c>d):
    print("c is the greatest number")
else:
    print("d is the greatest number")