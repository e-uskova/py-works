input()
s = str(input())
n = len(s)
u = [False] * n
num = 0
while s[0] != '-':
    i = 1
    while i < n:
        if s[i] == '#':
            if not u[i]:
                num += 1
                while s[i] == '#':
                    u[i] = True
                    i += 1
        elif u[i]:
            u[i] = False
        i += 1
    s = str(input())    
print(num)
