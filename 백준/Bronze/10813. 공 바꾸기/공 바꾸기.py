N, M = map(int, input().split())

x = []

for number in range(1, N + 1, 1):   # [1, 2, 3, 4, 5]
    x.append(number)

# print(x)
for line in range(M):
    i, j = map(int, input().split())
    tmp = 0                         # tmp 처음에는 0으로 설정

    tmp = x[i - 1]                  # tmp에 x의 i번째 수를 넣기
    x[i - 1] = x[j - 1]             # x의 i번째 수를 x의 j번째 수로 바꾸기
    x[j - 1] = tmp                  # x의 j번째 수를 tmp에 넣기
# print(x)
for i in x:
    print(i, end=' ')