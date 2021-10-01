testcase = int(input())
arr = [map(int, input().split()) for i in range(testcase)]

[print(i) for i in map(sum, arr)]

