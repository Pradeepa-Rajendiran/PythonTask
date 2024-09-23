name="Pradeepa"
def myname():
    print(name)
myname()

# function (global variable)
Name="Pradeepa"
def name():
    print("My Name is",Name)
name()
sin_number=23
def number():
    print("My sin number is",sin_number)
number()
College="SSCET"
def college():
    print("My college is",College)
college()
Place="Sankari"
def place():
    print("My place is",Place)
place()

# Local variable

def myhotel():
    name="Diya hotel"
    menus="Idly,Poori,Pongal,Vada"
    amount=20,50,50,20
    place="Tiruchengode"
    print("Hotel name is:",name)
    print("Menus are:",menus)
    print("Amount for food:",amount)
    print("venue of the hotel:",place)
myhotel()


# global keyword

def myage():
    global age
    age=20
    print(age)
myage()

# int conversion
print(int(10))
print(int(10.55))
print(int("10"))
print(int(True))
print(int(False))
# print(int("10.55"))  type error
# print(int("Jack123")) value error
# print(int(10+3j)) type error

# float conversion
print(float(10))
print(float(10.55))
print(float("10"))
print(float(True))
print(float(False))
# print(float("10.55"))  type error
# print(float("Jack123")) value error
# print(float(10+3j)) type error

# complex conversion
print(complex(10))
print(complex(10.55))
print(complex("10"))
print(complex(True))
print(complex(False))
# print(complex("10.55"))  type error
# print(complex("Jack123")) value error
print(complex(10+3j))

# string conversion
print(str(10))
print(str(10.55))
print(str("10"))
print(str(True))
print(str(False))
print(str("10.55"))
print(str("Jack123"))
print(str(10+3j))

# boolean conversion
print(bool(10))
print(bool(10.55))
print(bool("10"))
print(bool(True))
print(bool(False))
print(bool("10.55"))
print(bool("Jack123"))
print(bool(10+3j))
print(bool(0))

# length
a="Pyhton"
print(len(a))
# or
a="Pyhton"
i = len(a)
print(i)

# slice
name="Python"
x=name[2]
print(x)

name="Python"
x=name[2:]
print(x)

name="Python"
x=name[:2]
print(x)

name="Python"
x=name[2:5]
print(x)

# startswith,endswith,find,rfind
Name="Pyhton is a Programming Language"
print(Name.startswith("Py"))
print(Name.endswith("i"))
print(Name.upper())
print(Name.lower())
print(Name.find("m"))
print(Name.rfind("a"))
print(Name.count("i"))
print(Name.index("L"))
print(Name.rindex("m"))
print(Name.isupper())
print(Name.islower())
print(Name.strip())
# both are remove the space before or after the sentence

# remove left side space
print(Name.lstrip())
# remove right side space
print(Name.rstrip())

print(Name.isalnum())
print(Name.isnumeric())
print(Name.split(" "))
