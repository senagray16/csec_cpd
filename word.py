x = input()
u = 0
l = 0

for i in x:
    if i.upper() == i:
        u = u +1 
    else:
        l = l + 1 


if u > l:
    print (x.upper())
else:
    print (x.lower())
        
