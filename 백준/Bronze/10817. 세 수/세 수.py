from heapq import heapify, heappop

heap = list(map(int, input().split()))
heapify(heap)
# print(heap)

for _ in range(2) :
    min = heappop(heap)
    # print(min)
    # print(heap)
print(min)    