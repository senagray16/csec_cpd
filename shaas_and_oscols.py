x = int(input())
list = input().split()

for i in range(x):
    list[i] = int(list[i])

n = int(input())
for i in range(n):
    shot = input().split()
    for j in range(2):
        shot[j]= int (shot[j])
    
    shot[0] -=1
    if shot[0]==0 and shot[0]==x-1:
        list[shot[0]] = 0
    elif shot[0] == 0:
        r = list[shot[0]] - shot[1]
        list[shot[0]+1] += r
        list[shot[0]] = 0
    elif shot[0] == x-1:
        list[shot[0]-1] += shot[1]-1
        list[shot[0]] = 0
    
    else:
        r = list[shot[0]] - shot[1]
        list[shot[0]+1] += r
        l = shot[1]-1
        list[shot[0]-1] += l
        list[shot[0]] = 0

for y in list:
    print(y)
