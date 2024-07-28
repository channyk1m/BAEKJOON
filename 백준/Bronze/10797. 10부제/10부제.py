x = int(input())
y = input().split()

a = int(y[0])
b = int(y[1])
c = int(y[2])
d = int(y[3])
e = int(y[4])

n = 0

if x == a:
    n = n + 1
if x == b:
    n = n + 1
if x == c:
    n = n + 1
if x == d:
    n = n + 1
if x == e:
    n = n + 1

print(n)