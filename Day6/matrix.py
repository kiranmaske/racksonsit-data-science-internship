x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1,2,3],[4,5,6],[7,8,9]]
r = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len([x])):
        r[i][j]= x[i][j] + y[i][j]
for i in r:
    print(i)
    
# 2.Transpose
x = [[1,2],
     [4,5],
     [6,7]]
r = [0,0,0],[0,0,0]
for i in range(len(x)):
    for j in range(len[0]):
        r[j][i]=x[i][j]
for i in r:
    print(i)
    
# 3.copy all element

a1 = [1,2,3,4,5,6,7]
a2 = [None]*len(a1)
for i in range(0,len(a1)):
    print(a2[i],end=" ")
    
    
# 4. Duplicate element

a = [1,3,45,14,1,3,2,1,3,1]
# serarch duplicate element
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            print("duplicate element =",a[j])