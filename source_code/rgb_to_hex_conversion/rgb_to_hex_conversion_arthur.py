# author: Arthur
# date: 2018.12.18


def rgb(r, g, b):
    return ''.join(format(h, '02X') for h in (0 if num < 0 else 255 if num > 255 else num for num in (r, g, b)))

