a1 = input().split()
a2 = input().split()
a3 = input().split()
a4 = input().split()
a5 = input().split()

x = [a1,a2,a3,a4,a5]
a =0



for i in x:
    a = a+1
    b = 0
    for j in i:
        b = b+1
        if j == "1":
            c,f = a,b
            break
            

z = abs(c-3)+abs(f-3)
print (z)
            
