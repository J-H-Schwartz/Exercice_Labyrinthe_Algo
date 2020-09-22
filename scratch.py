table = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0]
]


# Tableau[Y][X]
# Monter: Y - 1 // Descendre: Y + 1
# Gauche: X - 1 // Droite : X + 1


def solver(y=0, x=0, already_passed=[]):
    already_passed.append([y, x])
    if table[y][x] == 2:
        return [[y, x]]
    pathes = is_pathes(y, x)
    for path in pathes:
        if path not in already_passed:
            goal = solver(path[0], path[1])
            if goal is not None:
                goal.append([y,x])
                return goal


def is_pathes(y, x):
    pathes = []
    if 0 < y + 1 < len(table) and table[y + 1][x] != 1:
        pathes.append([y+1, x])
    if 0 < y - 1 < len(table) and table[y - 1][x] != 1:
        pathes.append([y-1, x])
    if 0 < x + 1 < len(table[0]) and table[y][x + 1] != 1:
        pathes.append([y, x+1])
    if 0 < x - 1 < len(table[0]) and table[y][x - 1] != 1:
        pathes.append([y, x-1])
    return pathes


if __name__ == '__main__':
    path_to_goal = solver()
    for i in range(len(path_to_goal)-1, -1, -1):
        print(path_to_goal[i])
