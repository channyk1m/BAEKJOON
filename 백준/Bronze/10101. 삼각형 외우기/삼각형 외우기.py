a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    x = 'Error'
elif (a == b and a == c):
    x = 'Equilateral'
elif ((a == b) or (a == c) or (b == c)):
    x = 'Isosceles'
else:
    x = 'Scalene'

print (x)