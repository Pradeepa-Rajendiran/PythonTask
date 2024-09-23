# # class Solution:
# #     def printTriangle(self, N):
#
# # pattern problem
#
# n =int(input())
# for i in range(1, n+1, 1):
#      for j in range(1, i + 1):
#          print(j,end=" ")
#      print("")
#
# # # indentation pattern
# n =int(input())
# for i in range(1, n+1):
#      for j in range(1, n+1-i):
#          print(" ",end="")
#      for k in range(1,i+1):
#          print(k,end="")
#      print()
#
# # reverse pattern problem
# n =int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1-i):
#           print(" ",end="")
#     for k in range(i,0,-1):
#           print(k,end="")
#     print()


# n =int(input())
# for i in range(1, n+n,2):
#     for j in range(1, n+n-i):
#           print(" ",end="")
#     for k in range(1,i+1):
#           print(k,end=" ")
#     print()


n =int(input())
for i in range(1, n+n,2):
    for j in range(1, n+n-i):
         print(" ",end="")
    for k in range(1,i+1):
          print(k,end=" ")
    print()
for i in range(2*n-1, 0, -1):
   for j in range(n-i,0,-2):
      print(" ", end=" ")
   for k in range(1, i + 2):
       print(k, end=" ")
   print()