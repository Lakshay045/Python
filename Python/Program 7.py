# Grade Calculator

a = int(input("Enter the Marks of Physics : "))
b = int(input("Enter the Marks of Mathematics : "))
c = int(input("Enter the Marks of Chemistry : "))
d = int(input("Enter the Marks of Hindi : "))
e = int(input("Enter the Marks of English : "))

per = (a+b+c+d+e)/500*100

if(per>=95):
    print("Grade A+")
elif(per>=90 and per<95):
    print("Grade A") 
elif(per>=80 and per<90):
    print("Grade B")   
elif(per>=70 and per<80):
    print("Grade C")
elif(per>=60 and per<70):
    print("Grade D") 
else:
    print("Fail")       