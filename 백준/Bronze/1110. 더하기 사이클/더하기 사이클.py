n = int(input())
new = n
cnt = 0

while True :      
    one = new % 10
    ten = new // 10

    new = 10 * one + (one + ten) % 10

    cnt += 1
    if (n == new) :
        break
print(cnt)  