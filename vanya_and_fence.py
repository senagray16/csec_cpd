x = input().split()
y = input().split()
z=0

for i in range(int (x[0])):
    if int(y[i]) >int(x[1]):
        z = z+2
    else:
        z=z+1
        
print (z)
