num = int(input())
num_li = list(map(int, input().split()))
seat_li = []
cnt = 0

for i in num_li :
    if i not in seat_li :
        seat_li.append(i)
    else :
        cnt += 1

print(cnt)
