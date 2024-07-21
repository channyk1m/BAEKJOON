N = int(input())
M = list(map(int, input().split()))

M.sort()

print(M[0], M[N - 1])
# print(min(M), max(M))
