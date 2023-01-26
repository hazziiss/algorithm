num = int(input())

discard_li = []
num_li = list(range(1, num+1))

# print(num_li)
for i in range(num-1) :
    a = num_li.pop(0)
    discard_li.append(a)

    first = num_li.pop(0)
    num_li.append(first)

print(*discard_li, *num_li)