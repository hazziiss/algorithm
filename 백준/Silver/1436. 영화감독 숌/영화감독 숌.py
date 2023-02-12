n = int(input())
a = 0
cnt = 1

while True :
    b = str(a).replace('666','')

    if b != str(a) :
        # print(a)
        
        if cnt == n :
            print(a)
            break
        else :
            cnt += 1
            a += 1
    else :
        a += 1   