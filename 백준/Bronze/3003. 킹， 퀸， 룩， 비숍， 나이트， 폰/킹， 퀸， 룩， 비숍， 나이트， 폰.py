right = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))

for i in range(6):
    chess[i] = right[i] - chess[i]

for a in chess:                 # [1, 0, 0, 0, 0, 1] 형태의 리스트를 1 0 0 0 0 1 형태로 출력을 해준다
    print(a, end=' ')