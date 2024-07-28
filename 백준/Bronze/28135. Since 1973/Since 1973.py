n = int(input())
i, ans = 1, 0
while True:
    ans += 1
    if i == n:
        break
    if '50' in str(i):
        ans += 1
    i += 1
print(ans)