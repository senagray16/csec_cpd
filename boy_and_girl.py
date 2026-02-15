x = input()

y =[]


for i in x:
    if i in y:
        continue
    else:
        y.append(i)
        
        
c = 0
for i in y:
    c = c+ 1
    

if c % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
    
