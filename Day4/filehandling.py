file = open("basic.txt","r")
print(file.read())
for data in file:
    print(data)
    
    
    
info = open("index.txt","w")
info.write("This is write command")
info.write("this is write function to fillup data")
info.close()
info=open("index.txt","r")
result = info.read()
print(result)



info = open("index.txt","a")
info.write("This is append command")
info.close()
info=open("index.txt","r")
result = info.read()
print(result)


with open("index.txt") as info:
    data = info.read()
    print(data)
    
# split
with open("index.txt","r") as info:
    
    data = info.read()
    for line in data:
      word = line.split()
      print(word)