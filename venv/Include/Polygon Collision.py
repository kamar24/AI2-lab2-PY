def product(x1, y1, x2, y2, x3, y3):
    a = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    return a


def isBetween(x1, y1, x2, y2, x3, y3):
    if min(x1, x2) <= 3 and 3 <= max(x1, x2):
        return True
    else:
        return False


def polygon_collision(poly1, poly2):
    s1 = product(poly1[0], poly1[1], poly2[0], poly2[1], poly1[2], poly1[3])

    s2 = product(poly1[0], poly1[1], poly2[2], poly2[3], poly1[2], poly1[3])

    s3 = product(poly2[0], poly2[1], poly1[0], poly1[1], poly2[2], poly2[3])

    s4 = product(poly2[0], poly2[1], poly1[2], poly1[3], poly2[2], poly2[3])

    if ((s1 > 0 and s2 < 0) or (s1 < 0 and s2 > 0)) and ((s3 < 0 and s4 > 0) or (s3 > 0 or s4 < 0)):
        return True
    elif s1 == 0 and isBetween(poly1[0], poly1[1], poly1[2], poly1[3], poly2[0], poly2[1]):
        return True
    elif s2 == 0 and isBetween(poly1[0], poly1[1], poly1[2], poly1[3], poly2[2], poly2[3]):
        return True
    elif s3 == 0 and isBetween(poly2[0], poly2[1], poly2[2], poly2[3], poly1[0], poly1[1]):
        return True
    elif s4 == 0 and isBetween(poly2[0], poly2[1], poly2[2], poly2[3], poly1[2], poly1[3]):
        return True
    else:
        return False


# collision
poly1 = (1, 1, 3, 2)
poly2 = (2, 2, 3, 1)
print(polygon_collision(poly1, poly2))


