n = int(input())
l = [[*map(int, input().split())] for i in range(n)]
avg = [sum(arr[1:]) / arr[0] for arr in l]

for i in range(len(l)):
    cnt = 0    
    for j in l[i][1:]:
        if avg[i] < j:
            cnt +=1

    print("{0:0.3f}%".format(cnt / len(l[i][1:]) * 100))
