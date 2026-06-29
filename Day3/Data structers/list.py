# # list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# # print(type(list))
# # print(list)
# # list1 = []
# # print(type(list1))

# # list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
# # print(list[2])
# # print(list[-1])
# # list[1] = 2
# # print(list)

# month = [31,[28,20],31,30,30]

# print(month[1][0])  
# print(month[1])

# num = [23, 45, 67, 89, 12, 34 , 56, 78, 90, 11]
# print(num[2:5])  # Slicing the list to get elements from index 2 to 4
# print(num[2:])   # Slicing the list to get elements from index 2 to the end 
# print(num[:5])   # Slicing the list to get elements from the start to index 4
# print(num[:])

# metals =['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
# print(metals[2:5])  # Slicing the list to get elements from index 2 to 4
# print(metals[2:])   # Slicing the list to get elements from index 2 to the end

#builtin functions
num = [7,5,3,5,7,3,2,5,4,2]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sorted(num))

num = [0,0,0,False]
print(any(num))

num = [0,0,3,False]
print(any(num))

num = [0,0,3,False]
print(all(num))

num = [1,2,3,True]
print(all(num))

#builtin methods

num = [2,3,6,8,5,4,6,3,7,4]
num.append(0)
print(num)
num.insert(1,5)
print(num)
num.remove(5)
print(num)
x = num.pop()
print(x)
print(num.index(8))
print(num.count(3))
num.sort()
print(num)
num.reverse()
print(num)

#Reading and using elements

arr = []
n = int(input("Enter size of element :"))
for x in range(n):
    num = int(input("Enter elemenmts :"))
    arr.append(num)

print(arr)

even = [2 * i for i in range(1, 11)]  # Fixed the missing 'i' in the loop variable
print(even)