T = int(input())

for t in range(1, T+1) :
    p, q, r, s, w = map(int, input().split())


    a = p*w

    if r >= w :
        b = q
    else :
        b = q + (w-r) * s

    if a > b :
        print(f'#{t} {b}')        
    else :
        print(f'#{t} {a}')  