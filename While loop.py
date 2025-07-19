#while loop = a statement that will execute it's block of code,
#as long as its condition remains true
from pkg_resources import non_empty_lines

# while 1==1:
#     print("I am in loop")

# name = ""
# while len(name)==0:
#
#     name=input("Enter your name: ")
#     print("Hello " + name)

name = None
while not name:
    name = input("Enter your name: ")
    print("My name is: "+name)
