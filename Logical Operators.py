#logical operators(and,or,not) = used to check two or more conditional statements

temp = int(input("What is the temperature today? "))

if temp>0 and temp <30:
    print("Temperature is good today")
    print("Great climate")
elif temp<0:
    print("Its very cold outside")
elif temp>30:
    print("It's too hot outside")

