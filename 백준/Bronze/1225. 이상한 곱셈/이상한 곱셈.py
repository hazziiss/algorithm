import sys
a_str, b_str = sys.stdin.readline().split()

li_a = list(map(int,a_str))
# print(li_a)
li_b = list(map(int,b_str))

print (sum(li_a)*sum(li_b))
