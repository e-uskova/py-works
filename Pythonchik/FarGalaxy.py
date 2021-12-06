x = str(input())
d = {}
while ' ' in x:
    x = x.split()
    d[(float(x[0]), float(x[1]), float(x[2]))] = x[3]
    x = str(input())
max_d = 0
for i in range(len(d)):
    a = list(d.keys())[i]
    for j in range(i, len(d)):
        b = list(d.keys())[j]
        dist = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
        if dist > max_d:
            max_d = dist
            max_couple = [d[a], d[b]]
max_couple = sorted(max_couple)
print(max_couple[0], max_couple[1])
