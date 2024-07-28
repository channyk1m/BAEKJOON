n = int(input())
s = input()
U, O, S, P, C = 0, 0, 0, 0, 0
for i in range(n):
    if s[i] == 'u':
        U+=1
    elif s[i] == 'o':
        O+=1
    elif s[i] == 's':
        S+=1
    elif s[i] == 'p':
        P+=1
    elif s[i] == 'c':
        C+=1
print(min(U, O, S, P, C))