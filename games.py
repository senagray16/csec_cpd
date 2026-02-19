x = int(input())

y = []
for i in range(x):
    a = input().split()
    y.append(a)

a = 0
for i in y:
    x = y[:]
    x.remove(i)
    for j in x:
        if j[1]==i[0]:
            a = a+1 
            

print (a)
        
    
    
