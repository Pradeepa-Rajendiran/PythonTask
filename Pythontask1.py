# case sensitive
import sys
from wsgiref.simple_server import sys_version

a=40
A=20
print(a)
print(A)

# variable declaration
name="Ram"
_name="Jack"
my_name="Jonny"
MyName="Sam"
myName="Diya"
print(_name)
print(MyName)
print(my_name)
print(name)

# task1
MyName="R.Pradeepa"
sin_number="E21CS037"
dateof_birth="02-10-2024"
age=20
tenth_mark=428
twelfth_mark=538
phone_number=8344788588
print(MyName,'\n',sin_number,'\n',dateof_birth,'\n',age,'\n',tenth_mark,'\n',twelfth_mark,'\n',phone_number)
print(type("Pradeepa"))
print(type("E21CS037"))
print(type(20))
print(type(428.5))
print(type(538))
print(type(8344788588))


# datatype
a=10
b=12.45
c="deepa"
d=2+3j
type(a)
type(b)
type(c)
type(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# or otherwise
print(type(10))
print(type(4.43))
print(type(4+5j))
print(type("deepa"))

# with Name
Name="Pradeepa"
Age=20
print("My Name is",Name,"my age is",Age)
print("My Name is %s,my age is %d" %(Name,Age))

# raw data
print("C:Pradeepa\none\python")
print(r"C:Pradeepa\none\python")

# get input from user while run time

first_name=input("Enter the first name")
print("My first name is",first_name)
second_name=input("Enter the second name")
print("My Second name is",second_name)
mail_id=input("Enter the mail id")
print("My mailid is",mail_id)
phone_number=int(input("Enter your mobile number"))
print("My Phone number is",phone_number)
Dateof_birth=input("Enter your Date of birth")
print("My date of birth is",Dateof_birth)
Age=input("Enter your Age")
print("My Age is",Age)
Address=input("Enter Your Address")
print("My address is",Address)
pincode=int(input("Enter the your pincode"))
print("My pincode is",pincode)
mark_12=int(input("Enter Your mark in percentage"))
print("My 12th mark is",mark_12)
degree_mark=int(input("Enter your CGPA"))
print("My CGPA is",degree_mark)

# System version
print(sys_version)
print(sys.version)