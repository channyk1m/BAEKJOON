N = int(input())
SCORE = list(map(int, input().split()))     # map 앞에 list를 넣어주면 바로 list로 만들어줌

sum = 0
M = max(SCORE)

for i in range(N):
    sum += (SCORE[i]/M) * 100

print(sum / N)