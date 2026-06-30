# def show():
#     print("Hello Abhi")
# show()

# def sq(x):
#     y=x*x
#     print("Squ=",y)
    
# n=int(input("Enterno."))
# sq(n)


#  function returning value

# n=int(input("Enterno."))
# sq(n)

# def sq(x):
#     y=x*x
#     return y
# def cb(x):
#     y=x*sq(x)
#     return y

# print("Sq=",sq(n))
# print("cb=",sq(n))


# Default parametr

# def m(x=2,y=3,z=4):
#     r=x*y*z
#     return r
# print("MUl=",m())
# print("MUl=",m(5))
# print("MUl=",m(2,5))


# multi return

# def arr(n):
#     add=0
#     for x in n:
#         add+=x
#     avg = add//len(n)
#     return add,avg

# arr=[10,20,30]
# a,b = array(arr)
# print("Add=",a)
# print("Add=",b)


# Getting multiple parameters
 
# def show(*args):
#      for a in args:
#          print(a)
# show(1,2,3) 

# def show(**args):
#      for a in args:
#          print(a,args[a])
# display(name="Abhi",age="20")
















# map
def sq(n):
    return n*n
n = (1,2,3)
r=map(sq,n)
print(list(r))