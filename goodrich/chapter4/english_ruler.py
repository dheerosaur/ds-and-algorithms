
def draw_level(level):
    print('-' * level)


def draw_interval(levels):
    if levels == 0:
        return
    draw_interval(levels - 1)
    draw_level(levels)
    draw_interval(levels - 1)


def draw_ruler(start, end, levels):
    for i in range(start, end):
        print(('-' * (levels + 1)) + str(i))
        draw_interval(levels)
    print(('-' * (levels + 1)) + str(end))


draw_ruler(0, 2, 2)
