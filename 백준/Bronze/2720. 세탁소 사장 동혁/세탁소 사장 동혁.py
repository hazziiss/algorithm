T = int(input())

for t in range(1, T+1) :
    change = int(input())

    Q = change//25
    Q_ch = change%25
    D = Q_ch//10
    D_ch = Q_ch%10
    N = D_ch//5
    N_ch = D_ch%5
    P = N_ch//1

    print(Q, D, N, P)