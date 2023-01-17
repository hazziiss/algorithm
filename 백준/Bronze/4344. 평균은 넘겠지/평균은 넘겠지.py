T = int(input())

for t in range(T) :
    cnt = 0
    li = list(map(int, input().split()))
    n = li.pop(0)
    
    ave = sum(li)/n
    
    for i in li :
        if ave < i :
            cnt += 1   
    print('%.3f' %((cnt/n)*100) + '%')