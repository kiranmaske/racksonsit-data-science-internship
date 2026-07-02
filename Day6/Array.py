#  Array MOdule --> is an object

# 1.can store only one data type
# 2. size not fixed
# 3.







# 1 st- syntax
#  import array
#  arr=array.array("type code",[elements])
 
 
#  2nd Syntax
#   from array import*
#   arrayname = array("type code",[elements])


from array import *
a=array('i',[1,2,3,4,5,6,7])
# without index
for data in a:
    print(data,end="")
# with index 
size= len(a)
for data in range(size):
     print(a[data],end="")
     
# using while loop
from array import *
a = array('i',[1,2,3,4,5,6])
n = len(a)
i=0
while i<n:
    print(a[i])
    i+=1
    
# append function
from array import *
a = array('i',[1,2,3,4,5,6])
n = len(a)
i=0
while i<n:
    print(a[i],end="")
    i+=1
print("array after appending")
a.append(7)
a.append(8)
n = len(a)
i=0
while i<n:
    print(a[i],end="")
    i+=1
    
    
from array import *
a=array('i',[1,2,3,4,5])
a.insert(1,7)
print(a)
a.pop()
print(a)
a.remove(3)
print(a)
print(a.index(4))
a.reverse()
print(a)


# usere input using for loop

from array import *
arr =array('i',[])
n = int(input("Enter array size"))
for i in range(n):
    arr.append(int(input("Enter element")))
for i in range(len(arr)):
    print(arr[i],end=" ")
    
    
# extending array elements
from array import *
a = array('i',[1,2,3,4,5])
b = array('i',[6,7,8])
n = len(a)
i=0
while i<n:
    print(a[i],end=" ")
    i+=1
print("array after extending")
a.extend(b)
n = len(a)
i=0
while i<n:
    print(a[i],end=" ")
    i+=1

