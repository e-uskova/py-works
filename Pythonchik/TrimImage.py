rec = [0] * 5
rec = input().split()
masrec = []
x, y = map(int, rec[0:2])
left = right = x
up = down = y

while rec != ['0'] * 5:
    rec[0:4] = map(int, rec[0:4])
    if rec[2] != 0 and rec[3] != 0:
        left = min(rec[0], rec[0] + rec[2], left)
        right = max(rec[0], rec[0] + rec[2], right)
        up = min(rec[1], rec[1] + rec[3], up)
        down = max(rec[1], rec[1] + rec[3], down)
        masrec.append(rec)
    rec = input().split()

matrix = []
width = right - left
for i in range(down - up):
    matrix.append('.' * width)
for rec in masrec:
    if rec[2] < 0:
        rec[0] += rec[2]
        rec[2] = -rec[2]
    if rec[3] < 0:
        rec[1] += rec[3]
        rec[3] = -rec[3]
    rec[0] -= left
    rec[1] -= up

    for i in range(rec[1], rec[1] + rec[3]):
        matrix[i] = matrix[i][0:rec[0]] + rec[4] * rec[2] +\
                    matrix[i][rec[0] + rec[2]:width]
for i in matrix:
    print(*i, sep='')
