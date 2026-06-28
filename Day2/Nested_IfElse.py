num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))
num3 = int(input("Enter Third Number :"))

if num1 > num2:
    if num1 > num3:
        print("First Number is Greatest")
    else:
        print("Third Number is Greatest")
else:
    if num2 > num3:
        print("Second Number is Greatest")  
    else:
        print("Third Number is Greatest")