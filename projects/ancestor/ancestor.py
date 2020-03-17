def Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def create_graph(ancestors):
    graph = {}

    for pair in ancestors:
        key = pair[1]
        if key not in graph:
            graph[key] = set()
            graph[key].add(pair[0])
        else:
            graph[key].add(pair[0])
    return graph


print(create_graph([(1, 3), (2, 3), (3, 6), (5, 6),
                    (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]))


def earliest_ancestor(ancestors, starting_node):
    pass
