# 내가 쓴 풀이
# import sys

# num = int(sys.stdin.readline().rstrip())
# for i in range(num) :
#     print(sum(map(int, sys.stdin.readline().rstrip().split())))

for l in[*open(0)][1:] :
    print(sum(map(int,l.split())))