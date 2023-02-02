num = 1
summ = 0

for i in range(1, 6) :
    li = list(map(int, input().split()))
    # print(sum(li)) 

    if summ < sum(li) :
        summ = sum(li)
        max_num = num
        # print(num, summ, max_num) 
    num += 1
               

print(max_num, summ)        
