matrix = []

for _ in range(100) :
    temp = [0] * 100
    matrix.append(temp)

for _ in range(4) :
    x_1, y_1, x_2, y_2 = map(int, input().split())

    for i in range(x_1, x_2) :
        for j in range(y_1, y_2) :
            matrix[i][j] = 1

cnt = 0
for row in matrix :
    cnt += sum(row)
print(cnt)                    
