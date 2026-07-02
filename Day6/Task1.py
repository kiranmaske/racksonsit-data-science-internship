# 1.REverse order program using only for loop

x = [[5,6,7]]
r = [[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][len(x[0])-1-j]
for i in r:
    print(i)