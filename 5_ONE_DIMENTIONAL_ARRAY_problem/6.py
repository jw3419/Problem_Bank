# n = int(input())
# arr = [input() for i in range(n)]
# total= []

# for ox_str in arr:
#     t = 0
#     if ox_str[0] == 'O':
#         cnt = 1
#     else:
#         cnt = 0
#     t+=cnt
#     for j in range(1, len(ox_str)):
#         prev = ox_str[j-1]
#         curr = ox_str[j]
#         if curr=='O' and prev == curr:
#             cnt += 1
#         elif curr=='O':
#             cnt = 1 
#         else:
#             cnt = 0
#         t += cnt
#     total.append(t)
# [print(i) for i in total]

n,*l= input().split()
for i in l:
    n=0
    print( sum( (n:=(n+1)*(j=='O')) for j in i ) )