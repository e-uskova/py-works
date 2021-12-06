

def turtle(coord, direction):
    di = direction
    x, y = coord
    cmd = yield coord
    while cmd:
        if cmd == 'l':
            di = (di + 1) % 4
        elif cmd == 'r':
            di = (di + 3) % 4
        elif cmd == 'f':
            if di == 0:
                x += 1
            elif di == 1:
                y += 1
            elif di == 2:
                x -= 1
            elif di == 3:
                y -= 1
        cmd = yield x, y
