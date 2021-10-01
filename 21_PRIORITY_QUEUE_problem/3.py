from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap:
            num, sign = heappop(heap)
            print(num * sign)
        else:
            print(0)
    else:
        if x > 0:
            heappush(heap, (abs(x), 1))
        else:
            heappush(heap, (abs(x), -1))