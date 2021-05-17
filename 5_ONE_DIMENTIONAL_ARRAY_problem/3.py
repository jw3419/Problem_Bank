# 내가 쓴 풀이
# from typing import Counter

# dic = Counter(str(int(input()) * int(input()) * int(input())))
# [print(dic[str(i)]) for i in range(10)]

m=1
exec(3*'m*=int(input());')
for i in range(10):print(str(m).count(str(i)))