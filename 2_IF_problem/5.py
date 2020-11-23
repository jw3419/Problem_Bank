hours, minute = map(int, input().split())
# hours = 10
# minute = 10

minute = minute - 45
if minute < 0:
    if hours == 0:
        hours = 23
    else:
        hours = hours - 1
    minute = minute + 60
print(str(hours) + ' ' + str(minute))
