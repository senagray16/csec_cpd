x = int (input())
y = input()
a=0
d=0

for i in range(x):
    if y[i] == "A":
        a = a+1
    elif y[i] == "D":
        d = d + 1 
    
if a > d:
    print ("Anton")
elif d>a:
    print ("Danik")
else:
    print("Friendship")
    
