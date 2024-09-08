x = []
count = {}              # count라는 dictionary를 만든다{key:value, key:value}

for i in range(10):
    a = int(input())
    x.append(a % 42)

for i in x:
    try:                # 예외처리, 에러 우회. 코드를 테스트 하고 에러 발생시 except 실행
        count[i] += 1   
    except:             
        count[i]=1      
# print(count)
# print(x)
print(len(count))