a = list(input())
new_li = []

cam_li = ['C','A','M','B','R','I','D','G','E']
for i in a :
    if i not in cam_li :
        new_li.append(i)
print(*new_li,sep="")         