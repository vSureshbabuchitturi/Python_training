# print("Welcome Day2")

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for item in my_list:
#     item=item+1
#     print(item)
""""
my_list = [1, 2, 3]
print(my_list[0])
print(id(my_list))
my_list[0]=123
print(my_list[0])
print(id(my_list))
new_list = [81, 61, 31,1,1,2,2,3,3,4]
my_list3=my_list.copy()
print(my_list3)
#my_list.append(new_list)
print(my_list)
my_list.extend(new_list)
print(my_list)
my_list.remove(123)
print(my_list)
my_list.pop()
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(2))
print(my_list)
"""
from prompt_toolkit.key_binding.bindings.scroll import scroll_one_line_up

"""
my_list1=[]
my_list = [10, 20, 3, 4, 5, 6, 7, 8, 9]
for item in my_list:
    item=item+1
    my_list1.append(item)

print(my_list1)
"""
"""
x=11,12
print(type(x))
print("#"*20)
"""
"""
emp_date={10:'suri',20:'sure',30:'c'}
print(emp_date)
print(emp_date[10])
for item in emp_date:
    #print(item)
    print(item,emp_date[item])
"""
"""
emp_date={10:['suri','dev'],20:['suren','devops'],30:['suresh','BI'],}
print(emp_date[10][-1])
for item in emp_date:
    print(item,"=",emp_date[item][0],"=",emp_date[item][-1])

"""
"""
emp_date={10:('suri','dev'),20:['suren','devops'],30:['suresh','BI'],}
print(emp_date[10][-1])

x=[0,1,2,3,4,5,6,7,8,9,(1,23,34)]
print(x)
x.pop()

print(x)
x.append((10,1,1))
print(x)
"""
"""
emp_date={10:('suri','dev'),20:['suren','devops'],30:['suresh','BI'],}
x=emp_date.items()
print(x)
y=emp_date.keys()
print(y)
z=emp_date.values()
print(z)
# emp_date.popitem()
# emp_date.pop(20)
# for k,v in emp_date.items():
#     for i in v:
#         print(k,i)

print(40 in emp_date)
emp_date[40]='sony'
print(emp_date)
new={60:['suresh'],70:[],40:[]}
print(new)
emp_date.update(new)
print(emp_date)


new.setdefault(60,[])
print(new)
"""
"""
x={10,20,30,40,50,60,70,80,90,100}
y={10,20,30,40,50,60,70,80,90,10,200,400}

print(x.difference(y))
print(x.intersection(y))
y.difference_update(x)
print(y)
x.intersection_update(y)
print(x)
y.intersection_update(x)
print(y)
"""

"""
x=100
y=20
z=2
a=99
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>y and x>z)
print(x>y and not x<z)
print(x is a)

print(x==a+1)
print(x is 100)
"""
"""
x=int(input("Enter a number:"))
if x>0:
    print(f"{x} is positive")
else:
    print(f"{x} is negative")

print("End of program")

"""
"""
x=int(input("Enter a number:"))
if 99 < x < 1000:
    print(f"{x} is 3 digits")
else:
    print(f"{x} is not 3 digits")

print("End of program")
"""
"""
x=int(input("Enter a number:"))
if x>0:
    print(f"{x} is positive digits")
    if x%2==0:
        print(f"{x} is even number")
    else:
        print(f"{x} is odd number")
else:
    print(f"{x} is not positive number")

print("End of program")

"""
"""
i=10
while i>0:
    print(i)
    i=i-1
print("End of program")
"""

day1notes=open(r'D:\EV_Python_Training\DAY_1\day1_notes.txt',"r+")
day1notes.write("abccccccccccccccc")
# print(day1notes.read())
# print(type(day1notes))
x=day1notes.readlines()
for line in x:
    print(line.strip())

day1notes.close()