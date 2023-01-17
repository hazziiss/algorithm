T =  int(input())


for t in range(T) :
    add = 0
    summ = 0
    
    li = list(input())

    for i in li :
        if i == 'O' :
            add += 1
            summ += add
        else :
            add = 0   
    print(summ)         
