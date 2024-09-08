N, M = map(int, input().split())

x = []

for number in range(1, N + 1, 1):       # [1, 2, 3, 4, 5]
    x.append(number)

# print(x)
for line in range(M):
    i, j = map(int, input().split())
    tmp = 0                             # tmp 처음에는 0으로 설정

    for _ in range((j - i + 1) // 2):   # 패턴(1, 4 => 2    2, 8 => 3    이거에 충족하는 식을 찾아냄(j - i + 1) // 2)
        tmp = x[i - 1]
        x[i - 1] = x[j - 1]
        x[j - 1] = tmp

        i = i + 1                       # i가 시작... 뒤집기 때문에 i는 숫자가 하나씩 증가
        j = j - 1                       # j가 끝... 뒤집기 때문에 j는 숫자가 하나씩 줄음
#     print(x)
# print(x)
for i in x:
    print(i, end=' ')