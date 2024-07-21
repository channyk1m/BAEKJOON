N = int(input())
a = 1
for i in range(N):
    print(' ' * (N - 1), end="")    # 연산햇갈리지않기
    print('*' * a)
    N = N - 1
    a = a + 1