from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if heap and x == 0:
        print(heappop(heap))
    elif x > 0:
        heappush(heap, x)
    else:
        print(0)