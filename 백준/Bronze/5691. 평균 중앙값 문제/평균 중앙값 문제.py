while True :
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    if a == b == 0:
        break
    print(2 * a - b)