T = int(input()) # 테스트 케이스 수

for t in range(1, T+1) :
    # 두 수 입력받기
    a, b = list(map(int, input().split()))
    #print a b
    sh = a//b # 몫 계산
    re = a%b # 나머지 계산
    
    print(f"#{t} {sh} {re}")