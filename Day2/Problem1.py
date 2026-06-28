python = int(input("Enter Python Marks :"))
c = int(input("Enter C Marks :"))
cpp = int(input("Enter cpp Marks :")) 

print(python)
print(c)
print(cpp)

avg = (python + c + cpp)/3
if python < 35 or c < 35 or cpp < 35 or avg <= 40:
    print("You are FAil :")

else:
    print("You are Pass")