x = input().split()

a = int(x[0])
b = int(x[1])

if b >= 45:
    print(a, b - 45)
elif b < 45 and a > 0:
    print(a - 1, b + 15)
else:
    print('23', b + 15)
