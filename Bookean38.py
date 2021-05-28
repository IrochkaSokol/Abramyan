def Boolean38(x1, y1, x2, y2):
    s = False
    if x1 - x2 == y1 - y2 or x1 - x2 == y2 - y1:
        s = True
    return s