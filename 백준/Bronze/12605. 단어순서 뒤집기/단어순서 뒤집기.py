x = int(input())

for i in range(x):
    y = input().split()
    a = len(y)
    print('Case #' + str(i + 1) + ':', end = ' ')
    for i in range(len(y)):
        print(y[a - 1], end = ' ')
        a = a - 1
    print()
