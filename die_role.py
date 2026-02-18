y = input().split()
for i in range(2):
    y[i]=int(y[i])
    
x = 0
for i in range(2):
    if x < y[i]:
        x = y[i]
 
   
z = 1 + (6-x)
if z%2==0:
    if z%6 ==0:
        print(str(int(z/6))+"/1")
    else:
        print (str(int(z/2))+"/3")
elif z%3 == 0:
    print (str(int(z/3))+"/2")

else:
    print(str(z)+"/6")


