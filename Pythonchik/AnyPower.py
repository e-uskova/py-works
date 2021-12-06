import math

x = int(input())
i = 2
while i <= math.sqrt(x):
    if math.log(x, i) % 1 == 0:
        print('YES')
        break
    i += 1
if i > math.sqrt(x):
    print("NO")
