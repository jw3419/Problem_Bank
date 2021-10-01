h, m = map(int, input().split())
# print(['{0} {1}'.format(h, m-45), '{0} {1}'.format([h-1,24+(h-1)][h<1], 60+(m-45))][m<45])

print((h-(m<45))%24,(m-45)%60)