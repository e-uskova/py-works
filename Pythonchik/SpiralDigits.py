input_list = input().split(',')
w, h = (int)(input_list[0]), (int)(input_list[1])

a = [[0]*w for i in range(h)]
x = 0

for tmp in range(min(h // 2, w // 2)):
    for i in range(w - tmp * 2):
        a[tmp][i + tmp] = x % 10
        x += 1

    for i in range(tmp + 1, h - tmp):
        a[i][-tmp - 1] = x % 10
        x += 1

    for i in range(tmp + 1, w - tmp):
        a[-tmp - 1][-i - 1] = x % 10
        x += 1

    for i in range(tmp + 1, h - tmp - 1):
        a[-i - 1][tmp] = x % 10
        x += 1

if x < w * h:
    tmp = min( h // 2, w // 2)
    for i in range(w - tmp * 2):
        a[tmp][i + tmp] = x % 10
        x += 1

    for i in range(tmp + 1, h - tmp):
        a[i][-tmp - 1] = x % 10
        x += 1

for el in a:
    print(*el)
