# for i in "apple":
#     print(i)
from itertools import count

# for i in range(1,11):
#     print(i,"x2=",i*2)

# a=int(input("A:"))
# b=int(input("B:"))
# for i in range(a+1,b):
#     print(i)

# for i in range(1,11):
#     if (i%2==0):
#         print(i)

# count=0
# for i in range(1,5):
#     if (i%2==0):
#         count=count+1
# print(count)

# e_count=0
# o_count=0
# for i in range(1,11):
#     if (i%2==0):
#         e_count=e_count+1
#     else:
#         o_count=o_count+1
# print("Even_Count:",e_count)
# print("Odd_Count:",o_count)

# count=0
# for i in range(1,100):
#     if (i%3==0) & (i%5==0):
#         count=count+1
# print(count)

# for i in range(1,100):
#     if (i%3==0) & (i%5==0):
#         print(i)

# sum=0
# for i in range(6):
#     sum=sum+i
# print(sum)

a=[]
for i in range(5):
    num=int(input())
    a.append(num)
print(sum(a))
print(sum(a)/5)
