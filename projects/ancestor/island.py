from util import Stack, Queue


def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    # Check west
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    # Check east
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))

    return neighbors


def bft(x, y, matrix, visited):
    qq = Queue()
    qq.enqueue([x, y])
    while qq.size() > 0:
        v = qq.dequeue()
        x = v[0]
        y = v[1]
        if not visited[y][x]:
            visited[y][x] = True

            for neighbor in get_neighbors((x, y), matrix):
                qq.enqueue(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    counter = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = bft(x, y, matrix, visited)
                    counter += 1
    return counter


islands = [[0, 1, 0, 1, 0], [1, 1, 0, 1, 1], [
    0, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0]]


islands_2 = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
             [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
             [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
             [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
             [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands_2))
