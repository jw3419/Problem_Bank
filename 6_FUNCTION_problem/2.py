# def solve() :
#     exceptL = []
#     for i in range(1, 10001):
#         one = i % 10
#         anwer = i + one
#         if len(str(i)) == 2:
#             ten = i // 10
#             anwer += ten
#         elif len(str(i)) == 3:
#             ten = (i % 100) // 10
#             hun = i // 100
#             anwer += ten + hun
#         elif len(str(i)) == 4:
#             ten = (i % 100) // 10
#             hun = (i % 1000) // 100
#             thau = i // 1000
#             anwer += ten + hun + thau
#         exceptL.append(anwer)
#     exceptL.sort()
#     [print(i) for i in range(1, 10001) if i not in exceptL]

r=range(9999);
print(*sorted( {*r} - {n + sum(map(int,str(n))) for n in r} ))