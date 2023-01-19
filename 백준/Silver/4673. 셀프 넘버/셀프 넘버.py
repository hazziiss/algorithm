def d(n) :
    n = n + sum(map(int, str(n)))
    return n
nonSelf = set()

for i in range(1, 10001) :
    nonSelf.add(d(i))

for i in range(1, 10001) :
    if i not in nonSelf :
        print(i)