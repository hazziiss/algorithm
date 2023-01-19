def hansu (n) :
    li_int = list(map(int,str(n)))
    # print(li_int)
    
    if li_int[0] - li_int [1] == li_int[1] - li_int[2] :
        return 1   
        
    else :
        return 0            

n = int(input())
if n < 100 :
    print(n)


if n >= 100  :#and n != 1000 :
    cnt = 99
    for i in range(100, n+1) :
        result = hansu(i)
        cnt += result
    print(cnt)
