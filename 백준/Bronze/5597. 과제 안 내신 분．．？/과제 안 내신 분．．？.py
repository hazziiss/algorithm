li = []

for i in range(28) :
    a = int(input())
    li.append(a)
li.sort()

for i in range(1, 31) :
    if i not in li :  
        print(i)