"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Cannot create edge based on given vertices')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a Queue
        qq = Queue()
        # Create list of visited nodes
        visited = set()
        # Put starting node in queue
        qq.enqueue(starting_vertex)
        # While queue not empty
        while qq.size() > 0:
            # Pop first node out of queue
            vertex = qq.dequeue()
        # If not visited
            if vertex not in visited:
                # Mark as visited
                visited.add(vertex)
                print(vertex)
                # Get adjacent edges and add to list
                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)

        while stack.size() > 0:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for adjacent_node in self.get_neighbors(starting_vertex):
                self.dft_recursive(adjacent_node, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a Queue
        qq = Queue()
        # Add a path to the starting vertex_id to the queue
        qq.enqueue([starting_vertex])
        # Create and empty set to store visited nodes
        visited = set()
        # While the queue is not empty
        while qq.size() > 0:
            # Dequeue first path
            path = qq.dequeue()
            # Grab the last vertex from the path
            last_vertex = path[-1]
            # Check if it is the target
            if last_vertex == destination_vertex:
                # If true return the path
                return path
            # Check if it has been visited
            if last_vertex not in visited:
                # If false
                # Mark it as visited
                visited.add(last_vertex)
            # Then add a path to all neighbours to the back of the queue
                # Make a copy of the path before adding
                for neighbor in self.get_neighbors(last_vertex):
                    path_copy = path[:]
                    path_copy.append(neighbor)
                    qq.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack
        stack = Stack()
        # Push path to starting vertex to the stack
        stack.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # while stack is not empty
        while stack.size() > 0:
            # Pop first path
            path = stack.pop()
            # Grab last vertex from the path
            last_vertex = path[-1]
            # If last vertex matches dest vertex
            if last_vertex == destination_vertex:
                # Return path
                return path
            # If last vertex not in visited
            if last_vertex not in visited:
                # Mark as visited
                visited.add(last_vertex)
            # Then push paths to all neighbors to the top of the stack
                for neighbor in self.get_neighbors(last_vertex):
                    path_copy = path[:]
                    path_copy.append(neighbor)
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex == destination_vertex:
            return [starting_vertex]

        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                path = self.dfs_recursive(
                    neighbor, destination_vertex, visited)
                if path is not None:
                    return [starting_vertex] + path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('starting BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('starting DFT')
    graph.dft(1)
    print('Starting DFT recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('Starting BFS')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('Starting DFS')
    print(graph.dfs(1, 6))
    print('Starting DFS recursive')
    print(graph.dfs_recursive(1, 6))
