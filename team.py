n = int (input())
a = 0
for i in range(n):
    y = input().split()
    b = 0
    for i in y:
        if int (i) == 1:
            b = b+ 1
    if b >=2:
        a= a + 1

print (a)
            
    
    
