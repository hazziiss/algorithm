word = list(input())
new_li = []

while True :
    n = word.pop(0)
    new_li.append(n)

    if len(new_li) == 10 :
        print(*new_li,sep="")
        new_li = []
    if len(word) == 0:
        print(*new_li,sep="")
        break    