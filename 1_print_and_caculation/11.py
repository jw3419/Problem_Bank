a, b = list(map(int, input().split()))
one, ten, hun = b % 10, (b%100) // 10,  b//100
print(a*one, a*ten, a*hun, a*b, sep='\n')
