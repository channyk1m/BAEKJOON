N = int(input())
num = input()

num_list = list(map(int, num))  # map()은 돌아가면서 하나씩 숫자들을 int로 리스트를 만들고 나서 그 리스트의 메모리 주소를 리턴한다
                                # list()는 이 다음에 메모리 주소를 리스트 형태로 만들어준다
# print(num_list)

# sum = 0
# for i in range(N):
#     sum = sum + num_list[i]

# print(sum)

print(sum(num_list))