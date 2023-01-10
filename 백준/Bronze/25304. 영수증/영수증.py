tot = int(input())
n = int(input())
tot_t = 0

for i in range(n) :
    a, b = map(int, input().split())
    tot_t += (a * b)

if tot == tot_t :
    print('Yes')

else :
    print('No')   