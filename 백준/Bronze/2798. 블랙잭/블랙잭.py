n, m = map(int, input().split())
li = list(map(int, input().split()))
max_li = []

for i in range(len(li)-2) :
    for j in range(i+1, len(li)-1) :
        for k in range(j+1, len(li)) :
            summ = li[i]+li[j]+li[k]

            if summ <= m :
                max_li.append(summ)
print(max(max_li))                
                