times = int(input())

for t in range(1, times + 1):
    a, b = map(int, input().split())
    print("Case #{0}: {1}".format(t, a + b))
