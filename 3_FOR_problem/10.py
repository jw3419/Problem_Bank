times = int(input())

star = '*'
for time in range(times):
    # print('{0:>times}'.format(star))
    print(star.rjust(times))
    star = star + '*'
