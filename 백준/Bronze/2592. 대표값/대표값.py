from collections import Counter
li = []

for _ in range(10) :
    n = int(input())
    li.append(n)

many_num_li = Counter(li).most_common(1)
print(sum(li)//10 ,many_num_li[0][0], sep="\n")