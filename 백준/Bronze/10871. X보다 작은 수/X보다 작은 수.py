a = input().split()
b = input().split()

n = int(a[0])
x = int(a[1])


for i in range(n):
    b[i] = int(b[i])

for i in range(n):
    if b[i] < x:
        print(b[i], end=' ')