# Change values inside the function
from shlex import quote

X="Python"
def mydata():
    X="Java"
    print(X)
mydata()

# or to print global variable
X="Python"
def mydata():
    global X
    X="Java"
print(X)
mydata()

# Single and Double quote
print('"Java"')
print("'Python'")

# parametrized function
def myName(name):
    print("My Name is",name)
def myage(age):
    print("My age is",age)
myName("Pradeepa")
myage(20)

# task for parameterized function
def myname(Name):
    print("My name is",Name)
def myage(age):
    print("My age is",age)
def mycollege(cName):
    print("My college name is",cName)
def mymail(mail):
    print("My mail is",mail)
myname("Pradeepa")
myage(20)
mycollege("SSCET")
mymail("xyz@gmail.com")

# boolean values
print(10>5)
print(10==5)
print(10<20)

# conditional statements
time=input("Enter the time")
def mywishes():
    if time=="12AM":
        print("Good Morning")
    else:
        print("Good Afternoon")
mywishes()

ticket_booking=int(input("Enter the no.of.tickets"))
def tickets():
    if(ticket_booking<=10):
        print("Ticket is available")
    else:
        print("Ticket is not available")
tickets()

# logical operator
# AND Operator
age=int(input("Enter your age"))
gender=input("Enter your gender")
def schooljoining():
    if age>=5 and gender=="male":
        print("Eligible to join")
    else:
        print("Not Eligible to join")
schooljoining()

# OR operator
age=int(input("Enter your age"))
weight=int(input("Enter your weight"))
def policetraining():
    if age>=25 or weight>=50:
        print("Eligible to join")
    else:
        print("Not Eligible to join")
policetraining()

# task3
A=int(input("Enter A's height"))
B=int(input("Enter B's height"))
C=int(input("Enter C's height"))
def myfunction():
    if A>B and C<A:
        print("A is tallest")
    elif A<B and C<B:
        print("B is tallest")
    elif A<C and B<C:
        print("C is tallest")
    else:

        print("Enter the correct height")
myfunction()

# Looping statement
a=1
while a<=10:
    print(a)
    a+=1

a=10
while a>=1:
    print(a)
    a-=1

a=-10
while a<=10:
    print(a)
    a+=1

# 1)for loop without condition
for i in range(5):
    print(i)
print("----------------------------")
# 2)for loop with start and end point
for i in range(2,5):
    print(i)
print("----------------------------")
# 2)for loop with start and end point and increment
for i in range(1,10,3):
    print(i)

# task3
for i in range(11):
    print(i)
print("----------------------------")

for i in range(10,0,-1):
    print(i)
print("----------------------------")

for i in range(-10,10,1):
    print(i)
print("----------------------------")

# while loop odd
i=1
while(i<=10):
    if(i%2!=0):
        print(i)
    i+=1

# while loop even

i=1
while(i<=10):
    if(i%2==0):
        print(i)
    i+=1

# break condition
i=1
while(i<=10):
    print(i)
    if(i==5):
        break
    i+=1
