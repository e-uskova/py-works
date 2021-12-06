x = int(input())
res = x
x_sqr = x ** 2
rem = x_sqr % 10
index = 1
while x_sqr != x:
    res += rem * (10 ** index)
    x_sqr = x * rem + x_sqr // 10
    rem = x_sqr % 10
    index += 1
print(res)
