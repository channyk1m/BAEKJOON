T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)                    # 문자열에 들어있는 문자들을 모두 갈라놓기 위해서 쓰여지는 list()

    for x in range(len(S)):
        print((S[x]) * R, end='')  # end=''를 사용해서 한 줄로 출력
    print()                        # end='' 쓴 다음에는 출력할껀 다 출력하고 print()