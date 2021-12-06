s = str(input())
d = {}
while ' ' in s:
    s = s.split()
    if s[0] in d.keys():
        if s[1] not in d[s[0]]:
            d[s[0]].append(s[1])
    else:
        d[s[0]] = [s[1]]
    if s[1] in d.keys():
        if s[0] not in d[s[1]]:
            d[s[1]].append(s[0])
    else:
        d[s[1]] = [s[0]]
    s = str(input())
start = s
end = s = str(input())

def f():
    were = []
    were.append(start)
    search = [start] + d[start]
    while len(search) > 0:
        for seq in search:
            were.append(seq)
            search = [el for el in d[seq] if el not in were]
            var = d[seq]
            if end in var:
                return 'YES'
    return 'NO'
print(f())