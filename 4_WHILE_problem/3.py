count = 0
num = input()
answer = int(num)
while True:
    a = ['0'+num, num][int(num) > 10]
    tmp = sum(map(int, a))
    b = ['0'+str(tmp), str(tmp)][tmp > 10]
    num = a[-1] + b[-1]
    count += 1
    
    if answer == int(num): break

print(count)