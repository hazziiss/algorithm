import sys
a_str, b_str = sys.stdin.readline().split()

li_a = list(a_str)
li_b = list(b_str)

summ = 0

for i in li_a :
    for j in li_b :
        summ += int(i) * int(j)

print (summ)
