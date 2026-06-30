# # keywords








# print(10/2)
# print(20/5)
# print(10/0)
# print(80/2)
# print(40/5)
# print(10/5)
# print(10/3)

# a= int(input("enter 1st no."))
# b =in(input("enter 2nd no."))
# try:
#     a= a/b
# except ZeroDivisionError:
#     print("cant divide by zero")
#     exit(0)
# print("division=",a)



# handling multiple exception

try:
    a= int(input("enter 1st no."))
    b =int(input("enter 2nd no."))
    a= a/b
except ZeroDivisionError:
    print("cant divide by zero")
    exit(0)
except ValueError:
    print("cinvalid input")
    exit(0)
print("division=",a)

try:
    a=int (input("Enput 1st no."))
    b=int (input("Enput 2nd no."))
    a=a/b
except Exception as e:
    print("Error :",e)
    exit(0)
print("division=",a)

#finally
try:
    a=int (input("Enput 1st no."))
    b=int (input("Enput 2nd no."))
    a=a/b
except Exception as e:
    print("Error :",e)
    exit(0)
finally:
    print("Abhi")
    print("division=",a)

# 3.else
try:
    a=int (input("Enput 1st no."))
    b=int (input("Enput 2nd no."))
    a=a/b
except Exception as e:
    print("Error :",e)
    exit(0)
else:
    print("division=",a)
    
    
# 4.raise
num= int(input("Enter no"))
if num>100:
    raise Exception("Its a large no")


# 5.assert
def divide(n1,n2):
    assert n2!=0
    return n1/n2
a = int(input("enter 1st no."))
b = int(input("enter 2nd no."))

print("divide=",divide(a,b))



# collection module:
from collections import ChainMap
base = {'name':'Abhi','age':20}
adjust = {'age':20,'rno.':35}
print(list(ChainMap(adjust,base)))


import collections
d1 = collections.OrderedDict()
d1['A']=10
d1['B']=20
d1['C']=30

for k,v in d1.items():
    print(k,v)
    
    
import statistics
data=[1,58,6,4,6]
x= statistics.mean(data)
print("mean is=",x)
y= statistics.mode(data)
print("mode is=",y)