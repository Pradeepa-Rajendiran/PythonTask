# s=input("Enter the input string")
# count=0
# s=s.lower()
# for i in s:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         count+=1
# if count==0:
#     print("No Vowels")
# else:
#     print("" + str(count))
from Pythontask4 import count

n=input("Enter the input string")
s=set()
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if n[i]==n[j]:
            c=c+1
    if c>1:
        s.add(n[i])
print(len(s))
