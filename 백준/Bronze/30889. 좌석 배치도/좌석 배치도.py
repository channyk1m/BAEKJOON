n = int(input())
seat = [list('.' * 20) for i in range(10)]
for i in range(n):
    pos = input()
    row, col = ord(pos[0])-ord('A'), int(pos[1:])-1
    seat[row][col] = 'o'
for s in seat:
    print(''.join(s))