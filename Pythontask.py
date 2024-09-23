# def sum():
#     n=int(input("Enter the number"))
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# sum()
from array import array
from audioop import reverse

# text = "Hello, World!"
#
# reversed_text = text[::-1]
#
# print(reversed_text)

# n=int(input("enter the input"))
# for val in range(1,n+1):
#     for i in range(1,val+1):
#         print(i, end=" ")

# def factorial():
#     n=int(input("Enter the integer"))
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial()

# def statement():
#     arr=[2,4,1,3,5]
#     if(len(arr)<3):
#         print(-1)
#     else:
#         num1=arr[0]
#         num2=arr[1]
#         num3=arr[3]
#         if(num1>num2) and (num1>num3):
#             print(num1)
#         elif (num2>num1) and (num2>num3):
#             print(num2)
#         else:
#             print(num3)
# statement()


n=[1,2,3,4,5]
if n%2==0:
    print("even num")
else:
    print("Odd")
