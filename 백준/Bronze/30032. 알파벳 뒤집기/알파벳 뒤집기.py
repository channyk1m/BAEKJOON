def flip(a, d):
    if a == 'd':
        if d == 1:
            return 'q'
        else:
            return 'b'
    elif a == 'b':
        if d == 1:
            return 'p'
        else:
            return 'd'
    elif a == 'p':
        if d == 1:
            return 'b'
        else:
            return 'q'
    else:
        if d == 1:
            return 'd'
        else:
            return 'p'


n, d = map(int, input().split())
for i in range(n):
    s = input()
    for c in s:
        print(flip(c, d), end='')
    print()
