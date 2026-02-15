x = input().upper()
y = input().upper()

z = 0
for i in range(len(x)):
    if x[i] != y[i]:
        if x[i] > y[i]:
            z = 1
            break
        else:
            z = -1
            break
    
print (z)
