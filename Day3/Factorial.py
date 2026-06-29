num = int(input("Enter a number: "))
factorial = 1
if num <= 1:
    print("Factorial of", num, "is 1")
else:
    for i in range (2, num + 1):
        factorial = factorial * i
    print("Factorial of", num, "is", factorial)