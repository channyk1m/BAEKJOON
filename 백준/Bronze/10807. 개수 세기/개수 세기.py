n = int(input())
a = list(map(int, input().split()))
v = int(input())
ans = 0
for i in range(n):
    if a[i] == v:
        ans+=1
print(ans)