x = int(input())
a = 0
b = 0
for i in range(x):
    y = input().split()
    n = int(y[0])
    m = int(y[1])
    if n > m:
        a = a + 1
    if n < m:
        b = b + 1
    else:
        a = a + 0
print(a, b)