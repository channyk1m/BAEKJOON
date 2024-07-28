t = int(input())
n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    s += a[i]
if s >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")