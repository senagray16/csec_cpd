x = input().split()
for i in range(4):
    x[i] = int(x[i])
    
y = input()
f =[]

for i in y:
    f.append(int(i))
    
    
calory = 0
for i in f:
    calory = calory + x[i-1]
    
print (calory)
