x = int(input())
y = int(input())

z = 0

for i in range(y):
    a = input().split()
    b = int(a[0])
    c = int(a[1])
    z = z + (b * c)

if x == z:
  print("Yes")
else:
  print("No")
