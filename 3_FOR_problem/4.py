import sys  # sys모듈 읽어들이기
input = sys.stdin.readline
times = int(input())

for time in range(times):
    a, b = map(int, input().split())
    print(a + b)
