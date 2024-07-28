x = int(input())

while True:
    a = input()
    if a == "=":
        break
    b = int(input())
    if a == "+":
        x += b
    elif a == "-":
        x -= b
    elif a == "*":
        x *= b
    elif a == "/":
        x //= b
print(x)
