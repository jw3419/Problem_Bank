def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        if i < 100:
            cnt += 1
        else:
            arr = list(map(int, str(i)))
            if arr[0] - arr[1] == arr[1] - arr[2]:
                cnt +=1
    return cnt

print(hansu(int(input())))