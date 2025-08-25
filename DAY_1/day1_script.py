#testing Python comments
"""
First day
python training
"""
import math

""""
print("hi python")
print("Hello World hi suresh",sep=",", end="",flush=True)
a=10
print(a)
b=10

print(f"sum of a & b: {a+b}")

s_name='Suresh'
location='Hydrebad'
print(f"welcome {s_name} from {location}")
"""
""""
# input Function

s_name=input("Enter your name: ")
s_id=input("Enter your id: ")
s_location=input("Enter your location: ")

print(f"Name of Student {s_name} with id {s_id} from {s_location}")
"""
"""
# Mutable and Immutable
a=10
b=10
print(f"{a} and {id(a)}")

print(f"{b} and {id(b)}")

mylist=[1,2,3]
print(f"{mylist} and  id {id(mylist)}")

mylist1=[1,2,3]
print(f"{mylist1} and id {id(mylist1)}")
"""

# num1=eval(input("Enter a number: "))
# num2=eval(input("Enter another number: "))
#
# print(f"Sum of {num1} and {num2} is {num1+num2}")

# str1='hello'
# int1="hi i'am Suresh"
# print(str1[0])
# print(int1[-1:1])
# print(str1[0::2])
# print(str1[::-1])

userinfo="suresh:hyd:10001:345:/bin:/home"
x=["a",'b','c']

#print(userinfo.split(":")[0])
user_dob="j"
z="-".join(x)
print(z)