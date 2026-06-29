num = int(input("How many Students :"))
stud = []
for x in range(num):
    rollno = int(input("Enter Roll Number :"))
    name = input("Enter Name :")
    marks = float(input("Enter Marks :"))
    t = (rollno,name,marks)
    stud.append(t)
print(stud)    