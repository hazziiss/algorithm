h, m = map(int, input().split())
c = int(input())
new_m = m+c

while new_m >= 60 :
        new_m -= 60
        h += 1 

while h >= 24 :
    h -= 24
    
print(h, new_m)