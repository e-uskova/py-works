def checkhash(seq, f, mod):
    d = {}
    for s in seq:       
        if f(s) % mod in d.keys():
            d[f(s) % mod] += 1
        else:
            d[f(s) % mod] = 1
    return max(list(d.values())), min(list(d.values()))
