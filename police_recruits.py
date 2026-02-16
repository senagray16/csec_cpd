x= int (input())

y = input().split()
for i in range(x):
    y[i] = int(y[i])

s = 0
u = 0
for i in y:
    if i ==-1:
        if s == 0:
            u = u + 1
        else:
            s = s - 1 
         
    else:
        s = s + i
        
            
print (u)
