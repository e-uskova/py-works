s = str(input())
pat_list = input().split('@')

overlap = s.find(pat_list[0])
while overlap != -1:
    delim = overlap + len(pat_list[0]) + 1
    for part in pat_list[1:]:
        if part != s[delim: delim + len(part)]:
            break
        delim = delim + len(part) + 1
    else:
        break
    overlap = s.find(pat_list[0], overlap + 1)
print(overlap)
