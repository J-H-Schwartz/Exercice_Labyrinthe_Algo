table = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 1, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0]
]


class Counters:
    step_count = 0
    crossroads = []
    path = []


def solver_largeur(positions=[[0, 0]], already_passed=[], step=0):
    pathes = []
    step += 1
    print("Etape: {}".format(step))
    Counters.step_count += 1
    for position in positions:
        already_passed.append([position[0], position[1]])
        if table[position[0]][position[1]] == 2:
            return [position[0], position[1]], []
        table[position[0]][position[1]] = 3
        print("Nouvelle case testée: position x: {} y: {}".format(position[1], position[0]))
        for row in table:
            print(row)
    for position in positions:
        tmp_pathes = is_pathes(position[0], position[1], already_passed)
        for path in tmp_pathes:
            pathes.append(path)
    goal, tested = solver_largeur(pathes, step= step)
    for position in positions:
        tested.append("Etape {}, position vérifée: x: {} y: {}".format(step, position[1], position[0]))
    if goal is not None:
        return goal, tested


def solver(y=0, x=0, already_passed=[], tour=0):
    already_passed.append([y, x])
    tour +=1
    Counters.step_count += 1
    print(tour)
    print("Nouveau pas: positions {} {} ".format(x, y))
    if table[y][x] == 2:
        return [[y, x]]
    table[y][x] = 3
    for row in range(len(table)):
        print(table[row])

    pathes = is_pathes(y, x, already_passed)
    for path in pathes:
        goal = solver(path[0], path[1], tour=tour)
        if goal is not None:
            goal.append([y,x])
            return goal


def solver_iteratif(y=0, x=0):

    def pathes_counter(y, x):
        pathes_count = 0
        if y < len(table) - 1 and (table[y + 1][x] == 0 or table[y + 1][x] == 2):
            pathes_count += 1
        if y > 0 and (table[y - 1][x] == 0 or table[y - 1][x] == 2):
            pathes_count += 1
        if x < len(table[y]) - 1 and (table[y][x + 1] == 0 or table[y][x + 1] == 2):
            pathes_count += 1
        if x > 0 and (table[y][x - 1] == 0 or table[y][x - 1] == 2):
            pathes_count += 1
        return pathes_count

    def move(y, x):
        pathes_count = pathes_counter(y, x)
        if pathes_count > 1:
            Counters.crossroads.append([y, x])
        if y > 0 and (table[y - 1][x] == 0 or table[y - 1][x] == 2):
            y -= 1
            Counters.path.append([y, x])
        elif x > 0 and (table[y][x - 1] == 0 or table[y][x - 1] == 2):
            x -= 1
            Counters.path.append([y, x])
        elif y < len(table) - 1 and (table[y + 1][x] == 0 or table[y + 1][x] == 2):
            y += 1
            Counters.path.append([y, x])
        elif x < len(table[y]) - 1 and (table[y][x + 1] == 0 or table[y][x + 1] == 2):
            x += 1
            Counters.path.append([y, x])
        else:
            y = Counters.crossroads[len(Counters.crossroads) - 1][0]
            x = Counters.crossroads[len(Counters.crossroads) - 1][1]
            while Counters.path[len(Counters.path) - 1] != [y, x]:
                Counters.path.pop()
            Counters.crossroads.pop()
        return y, x

    while table[y][x] != 2:
        Counters.step_count +=1
        table[y][x] = 3
        for row in range(len(table)):
            print(table[row])
        y, x = move(y, x)

        print(f"Position actuelle: x: {x}, y: {y}")

    print(f"\nPosition finale: {x, y}")
    print(f"Nombre d'étapes totales: {Counters.step_count}")
    print("Chemin: ")
    final_path_count = 0
    for path in Counters.path:
        final_path_count +=1
        print("Case n°{}, Coordonnées: x:{} y: {}".format(final_path_count,path[1], path[0]))


def is_pathes(y, x, already_passed):
    pathes = []
    if 0 <= y - 1 < len(table) and table[y - 1][x] != 1 and [y-1, x] not in already_passed:
        pathes.append([y-1, x])
    if 0 <= x - 1 < len(table[0]) and table[y][x - 1] != 1 and [y, x - 1] not in already_passed:
        pathes.append([y, x-1])
    if 0 <= y + 1 < len(table) and table[y + 1][x] != 1 and [y+1, x] not in already_passed:
        pathes.append([y+1, x])
    if 0 <= x + 1 < len(table[0]) and table[y][x + 1] != 1 and [y, x + 1] not in already_passed:
        pathes.append([y, x + 1])
    return pathes


if __name__ == '__main__':

    # path_to_goal = solver()
    # goal_len = 0
    # print("Nombre total d'étapes: {}".format(Counter.step_count))
    # for i in range(len(path_to_goal)-1, -1, -1):
    #     goal_len +=1
    #     print("Pour le chemin le plus court, à l'étape {}, je suis passé sur la case x: {} y: {}"
    #           .format(goal_len, path_to_goal[i][1], path_to_goal[i][0]))
    # print("Longueur du chemin: {} cases".format(goal_len))

    # goal, tested = solver_largeur()
    # for i in range(len(tested)-1, -1, -1):
    #     print(tested[i])
    # print("Nombre total d'étapes: {}".format(Counter.step_count))
    # print("Le resultat est x: {} , y: {}".format(goal[1], goal[0]))

    solver_iteratif()



