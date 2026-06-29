num = {"a":"abc","b":"bcd","c":"cde"}
print(type(num))
print(num)
num2 = {1:"mon",2:"tue",3:"wed"}
print(type(num2))
print(num2)
print(num2[2])

data = ([1,56],[2,49],[6,75])
d = dict(data)
print(d)

animal = {}
print(type(animal))
animal[1] = "Dog"
animal[2] = "Cat"
animal[3] = "Elephant"
print(animal)

data = {2:45,5:38,6:11,7:105,9:20}
print(data.keys())
print(data.values())
print(data.items())

#set : is a collection of unique elements
s = {1,2,3,4,5,6,2,1}
print(s)

#emptyset

empset = set()
print(type(empset))

num = {21,23,32}
num.add(45)
print(num)

#update set

computer = {"HP","Dell","Lenovo"}
graphics = {"Acer","Nvidia","Ryzon"}

computer.update(graphics)
print(computer)