li = []
cnt = 1

for i in range(9) :
    a = int(input())
    li.append(a)

for i in li :
    if i != max(li) :
        cnt += 1
    else : 
        break
print(max(li)) 
print(cnt) 