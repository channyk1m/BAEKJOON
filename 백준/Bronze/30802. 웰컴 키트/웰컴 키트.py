import math

N = int(input())
a = list(map(int, input().split()))
t, p = map(int, input().split())
sum = 0
for i in a:
    sum += math.ceil(i/t)
print(sum)
print(N//p, N%p)