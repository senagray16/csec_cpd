x = input()

c= "a"
t =0

for i in x:
    a = abs(ord(c)-ord(i))
    if ord(c)>ord(i):
        b = (ord(i)-96)+(26-(ord(c)-96))
    else:
        b = (ord(c)-96)+(26-(ord(i)-96))
        
    if a > b:
        
        t +=b 
        c = i
    else:
        t+=a 
        c = i
    
print(t)
    
