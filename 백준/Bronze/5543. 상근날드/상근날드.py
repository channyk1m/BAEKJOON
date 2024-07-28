a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())

if a <= b and a <= c:
    x = a
elif b <= a and b <= c:
    x = b
else:
    x = c

if d <= e:
    y = d
else:
    y = e

print(x + y - 50)