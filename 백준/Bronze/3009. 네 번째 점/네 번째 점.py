x_li = []
y_li = []

for i in range(3) :
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)

for i in x_li :
    if x_li.count(i) == 1 :
        print (i, end= " ")
for i in y_li :
    if y_li.count(i) == 1 :
        print (i)       