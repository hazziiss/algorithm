T = int(input())

for t in range(1, T + 1) :

    num = list(map(int, input().split()))
    summ = 0 #입력받은 값들의 합

    for i in num :
        summ += i    
   
    print(f"#{t} {round(summ / 10)}") 