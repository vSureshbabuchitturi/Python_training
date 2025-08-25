#File Handling Seek method
with open (r'D:\EV_Python_Training\DAY_1\testfile.txt', 'r') as myfile:
    x=myfile.readlines()
    for i in x:
        print(i.strip())
    myfile.seek(0)
    print("#"*200)
    x1=myfile.read()
    print(x1)
print("end of file")
#Regular Expressions: re module
import re
with open (r'D:\EV_Python_Training\DAY_1\testfile.txt', 'w+') as myfile:
    x=myfile.readlines()
    print(x)
    print(myfile.tell())
    myfile.seek(0)
    print("#"*200)
    x1=myfile.read()
    print(x1)
print("end of file")
#Wildcards & Meta Characters in regex
import re
with open (r'D:\EV_Python_Training\DAY_1\testfile.txt', 'r') as myfile:
    for i in myfile:
        if re.search('[6-9][0-9]{9}',i):
            print(i.strip())

import re
with open (r'D:\EV_Python_Training\DAY_1\testfile.txt', 'r') as myfile:
    i=re.split("[0-9]",myfile.read())
    print(i)

import re
with open (r'D:\EV_Python_Training\DAY_1\testfile.txt', 'r') as myfile:
    for i in myfile:
        if re.search('[a-zA-z0-9][@][a-z]+[.][a-z]',i):
            print(i.strip())

import re
with open (r'D:\EV_Python_Training\DAY_1\testfile.txt', 'r') as myfile:
    for i in myfile:
        if re.search(r'\w+[@]\w+[.][a-z]$',i):
            print(i)

#Functions
def  f1(a):
    #a=input("enter your name:")
    print(f"hello:{a}")
f1("suresh")
print("out of function")
#f1()
#Functions global variables local
a=20
def f1(x,y):
    global c
    c=100
    return x+y+a

b=f1(2,3)
print(b)

def f2():
    z=200
    print(z+b+c)
f2()
print(f1(y=3,x=4))

#Functions Default values Keyword Arguments
def introduce(name,city,job="Admin"):
    print(f" Helloe {name} ur from  {city} with role {job}")

introduce("sursh","hyd","BI")

#Variable-Length Arguments (*args, **kwargs)
def f4(a,*b,**c):
    print(a)
    print(b)
    print(type(b))
    print(type(c))
    print(c)
    for i,j in c.items():
       print(i,j)
f4(10,3)
f4(2,3,4,5,6,7,89,9)
f4(2,3,4,5,z=20,v=40)

#Module
import testmodule as tm
k=tm.sum1(10,20)
print(k)
#Package and __init__.py
import mymath as mm

a=mm.mut(10,20)
print(a)



