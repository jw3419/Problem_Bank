# 내가 쓴 풀이
# arr = [int(input()) for i in range(9)]
# print(max(arr), arr.index(max(arr))+1)

print(*max((int(input()), i+1) for i in range(9)))