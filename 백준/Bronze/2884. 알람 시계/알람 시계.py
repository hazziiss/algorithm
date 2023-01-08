H, M = map(int, input().split())

if H > 0 :
    if (M >= 45) :
        M -= 45
    else :
        H -= 1
        M += 15
else :
    if (M >= 45) :
        M -= 45
    else :
        M += 15
        H = 23       

print(H, M)    