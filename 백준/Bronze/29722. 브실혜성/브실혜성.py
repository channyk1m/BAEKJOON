y, m, d = map(int, input().split('-'))
n = int(input())
for i in range(n):
    d += 1
    if d == 31:
        d = 1
        m += 1
        if m == 13:
            m = 1
            y += 1
print('%d-%02d-%02d'% (y, m, d))