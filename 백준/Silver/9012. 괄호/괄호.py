T = int(input())

for t in range(1,T+1) :
    li = input()
    stk = []
    aa = 1
    for i in li :
        if i == '(' :
            stk.append(i)
        else :
            if len(stk) == 0 :
                aa = 0
                break
            else :
                stk.pop()
    
    if len(stk) == 0 :
        if aa == 0: 
            print('NO') 
        else :
            print('YES')    
    else :
        print('NO')     