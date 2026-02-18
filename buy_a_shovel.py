x = input().split()

for i in range(2):
    x[i] = int(x[i])
    

for i in range(1,10):
    z= x[0]*i 
    z = str(z)
    c = z[-1]
    if c==str(x[1]) or c=='0':
        print (i)
        break
        
