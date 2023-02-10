a = int(input())
n= 1
for _ in range(1, 1000001) :
    N = [int(i) for i in str(n)]
    summ = n + sum(N)
    # print(summ)
    if summ == a :
        print(n)
        break
    elif n == 1000000 :
        print(0)
    else :
        n += 1