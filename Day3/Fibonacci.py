num = int(input("Enter Terms: "))
n1,n2 = 0,1
count = 0
if num <=1 :
    print("Invalid input")
else:
    print("Fibonacci sequence:")
    while count < num :
        print(n1 , end="  ")
        next = n1 + n2
        n1 = n2
        n2 = next
        count += 1

