T = int(input())

for t in range(1, T+1) :
    num_li = list(map(int, input().split()))

    print(f"#{t} {max(num_li)}")
