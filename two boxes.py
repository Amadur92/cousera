a2, b2, c2 = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())


def nb (x1, y1, z1, x2, y2, z2):
    return (x2 // x1) * (y2 // y1) * (z2 // z1)


a = max (nb(a1, b1, c1, a2, b2, c2), nb(a1, c1, b1, a2, b2, c2),
        nb(b1, a1, c1, a2, b2, c2), nb(b1, c1, a1, a2, b2, c2),
        nb(c1, a1, b1, a2, b2, c2), nb(c1, b1, a1, a2, b2, c2))
print(a)
