li = list(map(int, input().split()))

while True :
    if li[0] > li[1] :
        li[0], li[1] = li[1], li[0]
        print(*li)
    if li[1] > li[2] :
        li[1], li[2] = li[2], li[1]   
        print(*li)
    if li[2] > li[3] :
        li[2], li[3] = li[3], li[2]   
        print(*li)   
    if li[3] > li[4] :
        li[3], li[4] = li[4], li[3]   
        print(*li)           

    if li == [1, 2, 3, 4, 5] :
        break
