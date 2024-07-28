x = input().split()
c = int(input())

a = int(x[0])
b = int(x[1])

h = (a + (b + c) // 60)%24
m = (b + c) % 60

print(h, m)