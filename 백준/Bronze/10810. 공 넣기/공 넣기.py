N, M = map(int, input().split())    # 한 줄에 여러 숫자를 입력 받기(스페이스바로 기준 나누기)

x = []
for _ in range(N):
    x.append(0) # 리스트 제일 뒤에 값을 추가(N = 5: [0, 0, 0, 0, 0])

for line in range(M):
    i, j, k = map(int, input().split())
    y = i - 1   # y는 리스트에 몇번째 숫자를 바꿀지 고르는 값
    for b in range(j - i + 1):  # 반복문 안에 반복문을 넣어서 리스트에 숫자를 바꾸기
        x[y] = k    # 리스트x의 y번째 수는 k로 바뀐다
        y = y + 1

for i in x: # 리스트를 반복문에 넣는다
    print(i, end=' ')