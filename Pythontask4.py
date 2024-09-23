# nested for loop
for i in range(0,5,1):
    for j in range(0,5,1):
        print(i)

print("------------")

for i in range(1,5,2):
    for j in range(1,5,2):
        print(j)
print("------------")

# for each
for j in "Pradeepa":
    print(j)
from audioop import reverse
from dataclasses import replace
from os import remove

# Array
x=["Apple","Banana","Mango","Orange","Guava"]
print(x)

# index value
x=["Apple","Banana","Mango","Orange","Guava"]
print(x[0])

# length
x=["Apple","Banana","Mango","Orange","Guava"]
len1=len(x)
print(len1)

# append values
x=["Apple","Banana","Mango","Orange","Guava"]
append=x.append("Grapes")
# print(append)
print(x)

# replace values
x=["Apple","Banana","Mango","Orange","Guava"]
x[1]="Sapota"
print(x)

# pop
x=["Apple","Banana","Mango","Orange","Guava"]
x.pop(0)
print(x)

# remove
x=["Apple","Banana","Mango","Orange","Guava"]
x.remove("Banana")
print(x)

# count
count=x.count("Banana")
print(count)

# index of given value
index=x.index("Guava")
print(index)

# insert in b/w elements
x.insert(2,"Muskmelon")
print(x)

# reverse
x.reverse()
print(x)

# sort based on muskmelon
x.sort()
print(x)
from operator import index

# list
l=["Carrot","Beetroot",2,2.4,"Cabbage"]
print(l)

# slice operator
l=["Carrot","Beetroot",2,2.4,"Cabbage"]
print(l[4])

# index
index=l.index("Carrot")
print(index)


index=l.index(2,1)
print(index)


index=l.index(2.4,0,5)
print(index)


# class,methods,object
class School:
    def present(self):
        print("Akil is present")
    def absent(self):
        print("Balaji is absent")
rec=School()
rec.present()
rec.absent()

# single inheritance
class Teacher:
    def teacherName(self):
        print("Jack")

class Student(Teacher):
    def studentName(self):
        print("Max")
s=Student()
s.studentName()
s.teacherName()

print("------------")

# multilevel inheritance
class Teacher:
    def teacherName(self):
        print("Jack")

class Student(Teacher):
    def studentName(self):
        print("Max")

class Address(Student):
    def location(self):
        print("Chennai")
a=Address()
a.teacherName()
a.studentName()
a.location()

print("------------")

# multiple inheritance
class Teacher:
    def teacherName(self):
        print("Jack")

class Student():
    def studentName(self):
        print("Max")

class Address(Student,Teacher):
    def location(self):
        print("Chennai")
a=Address()
a.teacherName()
a.studentName()
a.location()

print("------------")