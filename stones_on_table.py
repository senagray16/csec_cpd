n = int (input())
x = input()

r=0
y =[]
for i in range(1,n):
    if x[i]==x[i-1]:
        r +=1
        
        

print (r)
