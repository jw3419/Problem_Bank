# a, b = map(int, input().split()) #여기서 런타임 에러가 나는듯...
a = int(input())
b = int(input())


hundred = b // 100
ten = (b - (hundred * 100)) // 10
one = b % 10

print(a * one)
print(a * ten)
print(a * hundred)
print(a * b)
