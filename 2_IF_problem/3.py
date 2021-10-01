num = int(input())
print('01'[(num%4==0 and num%100!=0) or num%400==0])