N = int(input())
for i in range(0, N, 1):           # 줄 수
    for j in range(0, i, 1):    # 공백을 한 줄에 찍기
        print(' ', end='')
    for k in range(i, N, 1):    # 별을 한 줄에 찍기
        print('*', end='')
    print()                         # end=''을 쓰면 꼭 print()를 해라