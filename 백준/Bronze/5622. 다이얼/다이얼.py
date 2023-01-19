MUNJA = list (input())
time = 0

for i in MUNJA :
    
    # print(i)
    if ord(i) in range(65, 68) : #2
        time += 3
    if ord(i) in range(68, 71) :
        time += 4
    if ord(i) in range(71, 74) : #4
        time += 5
    if ord(i) in range(74, 77) :
        time += 6
    if ord(i) in range(77, 80) : #6
        time += 7
    if ord(i) in range(80, 84) :
        time += 8
    if ord(i) in range(84, 87) : #8
        time += 9
    if ord(i) in range(87, 91) :
        time += 10
    # print(time)               
print(time)
