import copy

x = int(input())
x_copy = copy.copy(x)
y = 0

if x % 10 == 0:
    print('NO')
else:
    while x > 0:
        digit = x % 10
        x = x // 10
        y = y * 10 + digit
    if x_copy == y:
        print('YES')
    else:
        print('NO')
