x = list(input())
# print(x)
# print(len(x))
# print()

num = 0

for i in range(len(x)):
    if((x[i] == 'A') or (x[i] == 'B') or (x[i] == 'C')):        # if(x[i] == 'a' or 'b' or 'c')를 해버리면 빈 문자가 아닌 이상 ''랑 "" 빼고 싹다 true 이어서 따로따로 하나씩 true or false를 해주기 위해서 ==을 써야한다
        num = num + 2
    elif((x[i] == 'D') or (x[i] == 'E') or (x[i] == 'F')):
        num = num + 3
    elif((x[i] == 'G') or (x[i] == 'H') or (x[i] == 'I')):
        num = num + 4
    elif((x[i] == 'J') or (x[i] == 'K') or (x[i] == 'L')):
        num = num + 5
    elif((x[i] == 'M') or (x[i] == 'N') or (x[i] == 'O')):
        num = num + 6
    elif((x[i] == 'P') or (x[i] == 'Q') or (x[i] == 'R') or (x[i] == 'S')):
        num = num + 7
    elif((x[i] == 'T') or (x[i] == 'U') or (x[i] == 'V')):
        num = num + 8
    elif((x[i] == 'W') or (x[i] == 'X') or (x[i] == 'Y') or (x[i] == 'Z')):
        num = num + 9

print(num + len(x))
