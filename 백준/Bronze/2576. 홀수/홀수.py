li = []
for _ in range(7) :
    n = int(input())
    li.append(n)
# print(li)    
odd_li =  []

for i in li :
    if i % 2 != 0 :
        odd_li.append(i)
if len(odd_li) == 0 :
    print('-1')        
else :
    print(sum(odd_li), min(odd_li),sep="\n")       