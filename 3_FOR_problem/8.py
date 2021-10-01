# 내가 쓴 풀이
# for i in range(int(input())): 
#     a, b = map(int, input().split())
#     print('Case #%d: %d + %d = %d' %(i+1, a, b, a+b))


i=0
for a,_,c,_ in[*open(0)][1:]:i+=1;print(f'Case #{i}:',a,'+',c,'=',int(a)+int(c))