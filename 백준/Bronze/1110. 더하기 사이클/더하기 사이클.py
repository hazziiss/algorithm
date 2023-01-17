n = int(input()) #26
new = n #26
cnt = 0

while True :
    one = new % 10 #6
    ten = new // 10 #2
    new = one*10 + (one+ten)%10 #68
    # print(new)
    cnt += 1

    if n == new :
        break

print(cnt)  