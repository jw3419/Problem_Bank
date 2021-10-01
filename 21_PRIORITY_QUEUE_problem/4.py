## 원소를 받는대로 minheap에 추가
## mid = int(len(heap) / 2)
## tmp = minheap.copy()
## [heappop(tmp) for i in range(mid+1)]
## 1. heap의 길이가 짝수인지 홀수인지 확인
    ## 1-1. heap이 짝수면, print(min(answer[mid-1: mid+1]))
    ## 1-2. heal이 홀수면, print(answer[mid])

from heapq import heappop, heappush
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    heappush(heap, x)
    mid = int(len(heap) / 2)
    tmp = heap.copy()
    answer = [heappop(tmp) for _ in range(mid + 1)]

    if len(heap) % 2 == 0:
        print(min(answer[mid-1: mid+1]))
    else:
        print(answer[mid])