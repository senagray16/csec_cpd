n  = int (input())
y = input().split()

for i in range(n):
    y[i]=int(y[i])


s=0
d=0
c=n 
f = 0
for i in range(n):
    a = y[f]
    b=y[c-1]
 
    
    if i%2==0:
        if a>b:
            s = s + a
            f = f + 1 
        else:
            s = s + b 
            c = c - 1
    else:
        if a>b:
            d = d + a
            f = f + 1 
        else:
            d = d + b 
            c = c - 1
            

print (str(s) + ' ' + str(d))
        
        
    
