T = int(input())

for _ in range(T) :
    li = list(map(int, input().split()))
    li = sorted(li)
    # print(li)
    tot_li = [li[1], li[2], li[3]]

    if max(tot_li) - min(tot_li) >= 4 :
        print('KIN')
    else :
        print(sum(tot_li))    