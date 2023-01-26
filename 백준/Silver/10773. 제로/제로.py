T = int(input())
num_li = []

for t in range(1, T+1) :
    num = int(input())

    if num == 0 :
        num_li.pop()
    else :    
        num_li.append(num)
print(sum(num_li))        