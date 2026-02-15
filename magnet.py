x = int(input())
arr =[]

for i in range(x):
    y = input()
    arr.append(y)


g =0 
last = ""
for i in arr:
    if g == 0:
        g = 1
        last = i
    else:
        if i == last:
            continue
        else:
            last = i
            g = g +1 
            

print (g)
    
        
