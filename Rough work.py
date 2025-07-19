# name=input()
# age=int(input())
# print("My Name is: ",name)
# print("My age is: ",age)

# a=int(input())
# b=int(input())
# c=int(input())
# Mul=a*b*c
# Add=a+b+c
# Div=Mul/Add
# print("Multiplication of 3 numbers: ",Mul)
# print("Addition of 3 numbers: ",Add)
# print("Division of result: ",Div)

# Meghna=input("Status:Died/Alive\n")
# if (Meghna=="alive"):
#     print("She will weds surya")
# else:
#     print("Surya will go")

# Mark=int(input("Enter yor Mark: "))
# if Mark>35:
#     print("Pass")
# else:
#     print("Fail")

# Income = int(input("Enter yor Income: "))
# if Income > 7000:
#     print("Scholarship is available")
# else:
#     print("Not eligible for Scholarship")

# Number=int(input("Enter the number:"))
# if Number%3==0 & 5==0:
#     print("The number is divisible by 3 and 5")
# else:
#     print("The number is not divisible by 3 and 5")

# Get input for the number and find it is odd or even
# Yes = int(input("Enter the number: "))
# if(Yes%2==0):
#     print("The number is EVEN")
# else:
#     print("The number is ODD")

# Score=int(input("Enter Mark out of 100: "))
# Mark=Score
# if (Mark<35):
#     print("Poor Student")
# elif (Mark>35) & (Mark<70):
#     print("Average student")
# elif (Mark>70) & (Mark<100):
#     print("Good student")
# else:
#     print("Invalid")

# a=int(input("A: "))
# b=int(input("B: "))
# c=input("(+,-,*,/): ")
# if (c== "+"):
#     print(a+b)
# elif (c=="-"):
#     print(a-b)
# elif (c=="*"):
#     print(a*b)
# elif (c=="/"):
#     print(a/b)

# Salary = int(input("Enter your salary: "))
# Age = int(input("Enter your age: "))
# if (Salary>=20000) | (Age<=25):
#     print("You are eligible for loan")
#     Loan = int(input("Enter you loan amount: "))
#     if Loan<=50000:
#         print("Loan amount of",Loan, "is processed")
#     else:
#         print("Amount is greater than 50000")
# else:
#     print("You are not eligible for loan")


Maths=int(input("Maths:"))
English=int(input("English:"))
Tamil=int(input("Tamil:"))
Science=int(input("Science:"))
Social=int(input("Social:"))
Average=(Maths+English+Tamil+Science+Social)/5
if  Average<=45:
    print("Your average score is: ",Average,"Additional classes required")
else:
    print("Your average score is: ",Average,"Keep improving")




