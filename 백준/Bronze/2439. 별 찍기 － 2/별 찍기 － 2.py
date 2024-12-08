# N = int(input())
# a = 1
# for i in range(N):
#     print(' ' * (N - 1), end="")    # 연산햇갈리지않기
#     print('*' * a)
#     N = N - 1
#     a = a + 1



N = int(input())
for i in range(N, 0, -1):           # 줄 수
    for j in range(0, i - 1, 1):    # 공백을 한 줄에 찍기
        print(' ', end='')
    for k in range(i - 1, N, 1):    # 별을 한 줄에 찍기
        print('*', end='')
    print()                         # end=''을 쓰면 꼭 print()를 해라
