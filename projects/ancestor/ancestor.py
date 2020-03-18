class Queue():
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


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
             (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(create_graph(ancestors))

# Test Graph
# {3: {1, 2}, 6: {3, 5}, 7: {5}, 5: {4}, 8: {11, 4}, 9: {8}, 1: {10}}

'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''


def get_earliest_ancestor(ancestors, starting_node):
    graph = create_graph(ancestors)
    qq = Queue()
    qq.enqueue([starting_node])
    earliest_path = None

    while qq.size() > 0:
        path = qq.dequeue()
        current_node = path[-1]


get_earliest_ancestor(ancestors, 3)
