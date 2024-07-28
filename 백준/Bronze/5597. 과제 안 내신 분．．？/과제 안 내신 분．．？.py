check = [False]*31
for i in range (28):
    a = int(input())
    check[a] = True
for i in range (1, 31):
    if check[i] == False:
        print(i)