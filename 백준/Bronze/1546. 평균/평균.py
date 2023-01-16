T = int(input())
new_li = []

li = list(map(int, input().split()))
m = max(li)

for i in range(len(li)) :
    new = li[i] / m * 100
    new_li.append(new)
print(sum(new_li)/T)    