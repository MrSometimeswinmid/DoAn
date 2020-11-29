import random

LIST_COLORS = []

def remove_color(doppelganger):
    if doppelganger in LIST_COLORS:
        LIST_COLORS.remove(doppelganger)

def hex_code_colors():
    z = ''
    while z not in LIST_COLORS:
        a = hex(random.randrange(0,256))
        b = hex(random.randrange(0,256))
        c = hex(random.randrange(0,256))
        a = a[2:]
        b = b[2:]
        c = c[2:]
        if len(a)<2:
            a = "0" + a
        if len(b)<2:
            b = "0" + b
        if len(c)<2:
            c = "0" + c
        x = a + b + c
        z = "#" + x
        if z in LIST_COLORS:
            continue
        if z == "#000000" or z == "#FFFFFF":
            continue
        LIST_COLORS.append(z)
        return z




