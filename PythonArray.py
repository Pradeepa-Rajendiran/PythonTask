print("Enter the number")
n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
for i in range(0,n):
    print(a[i])
even=sorted(a[::2])
a[::2]=even
print(a)