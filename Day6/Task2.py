# 2. largest element
a = [4,2,6,9,4,3,1,7,9]
big = a[0]
for i in range(1, len(a)):
    if a[i] > big:
        big = a[i]
print("Largest number is :", big)