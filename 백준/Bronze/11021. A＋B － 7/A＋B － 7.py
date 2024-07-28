x = int(input())

for i in range(x):
    y = input().split()
    a = int(y[0])
    b = int(y[1])
    print("Case #" + str(i + 1) +": "+ str(a + b))
