a, b, c = int(input()), int(input()), int(input())
if ((a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0)) and\
   ((a % 2 != 0) or (b % 2 != 0) or (c % 2 != 0)):
    print('YES')
else:
    print('NO')
