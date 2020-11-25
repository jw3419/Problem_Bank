times = int(input())

for time in range(1, times + 1):
    a, b = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(time, a, b, a + b))
