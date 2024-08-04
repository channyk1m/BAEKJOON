num = []

for i in range(9):
    a = int(input())
    num.append(a) # 제일 뒤에 추가 하기(append) | 리스트 이름.append(추가할 값) |

m = max(num) # 리스트의 최대값 찾기 | max(리스트 이름) |
print(m)
print(num.index(m) + 1)