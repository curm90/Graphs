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

# print(create_graph(ancestors))

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


# NOT WORKING
def earliest_ancestor(ancestors, starting_node):
    # Build graph
    graph = create_graph(ancestors)
    # create a queue
    qq = Queue()
    # enqueue starting node inside a list
    qq.enqueue([starting_node])
 # set initial earlyest ancestor
    earliest_ancestor = -1
    # set a max path length to 1
    path_length = 1

    # while queue has contents
    while qq.size() > 0:
        # dequeue the path
        path = qq.dequeue()
        # get the last vert
        node = path[-1]

        # if path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= path_length and node < earliest_ancestor) or (len(path) > path_length):
            # set the earliest ancestor to the vert
            earliest_ancestor = node
            # set the max path length to the len of the path
            path_length = len(path)
        # loop over each neighbor in the graphs vertices at index of vert
        for neighbor in graph[node]:
            # make a copy of the path
            path_copy = list(path)
            # append neighbor to the coppied path
            path_copy.append(neighbor)
            # then enqueue the copied path
            qq.enqueue(path_copy)
    # return earliest ancestor
    return earliest_ancestor


print(earliest_ancestor(ancestors, 3))
