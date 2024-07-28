x = input().split()

a = int(x[0])
b = int(x[1])
c = int(x[2])

if a == b == c:
    print(a * 1000 + 10000)
elif a == b:
    print(a * 100 + 1000)
elif a == c:
    print(a * 100 + 1000)
elif b == c:
    print(b * 100 + 1000)
elif a > b and a > c:
    print(100 * a)
elif b > a and b > c:
    print(100 * b)
else:
    print(100 * c)