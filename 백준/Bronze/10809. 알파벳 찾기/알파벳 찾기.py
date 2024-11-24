S = input()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(S)):                         
    # print(alphabet.index(S[i]), S.index(S[i]))  # S의 i번 에 있는 문자를 alphabet 리스트에서 찾아서 인덱스 번호를 출력, S의 i번에 있는 문자의 순서를 찾아서 출력
    # index()는 괄호 안에 들어있는 문자열 또는 숫자가 다른 문자열 또는 리스트의 몇번째 인덱스인지를 확인
    try:                                                
        alphabet[alphabet.index(S[i])] = S.index(S[i])
    except:                                             # 에러가 난다면 그냥 컨틴뉴
        continue

for i in range(len(alphabet)):                          # 문자를 모두 -1로 바꿔주기 위해서 반복
    try:
        alphabet[i] + 1                                 # +1을 했는데 에러가 나면 숫자가 아니라는 것 --> 에러남
    except:
        alphabet[i] = -1                                # 에러가 난다면 -1로 바꿔줌
print(*alphabet)