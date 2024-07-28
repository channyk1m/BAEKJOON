n, k, p = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(0, n*k, k):
    if sum(a[i:i+k])>k - p:
        ans+=1
print(ans)