x = input().split()
for i in range(4):
    x[i] = int(x[i])

y = []
for i in x:
    if i in y:
        continue
    else:
        y.append(i)

n = len(y)
print(4-n)
