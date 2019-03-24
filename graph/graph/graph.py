import abc
from queue import Queue

import numpy as np


class Graph(abc.ABC):

    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertex_id == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight != 1:
            raise ValueError("An adjaceny set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if self.directed is False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)

        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.num_vertices):
            if v in self.get_adjacent_vertices(i):
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, '-->', v)


def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.num_vertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue

        print("Visit: ", vertex)

        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)


def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return

    visited[current] = 1
    print("Visit: ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


def topological_sort(graph):
    queue = Queue()

    indegree_map = {}

    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree(i)

        # Queue all nodes which have no dependencies i.e.
        # no edges coming in
        if indegree_map[i] == 0:
            queue.put(i)

    sorted_list = []
    while not queue.empty():
        vertex = queue.get()

        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] -= 1

            if indegree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This graph has a cyccle!")

    print('Topological sorted order:', sorted_list)


if __name__ == '__main__':

    def test_graph(g):
        for i in range(g.num_vertices):
            print("Adjacent to: ", i, g.get_adjacent_vertices(i))

        for i in range(g.num_vertices):
            print("Indegree: ", i, g.get_indegree(i))

        for i in range(g.num_vertices):
            for j in g.get_adjacent_vertices(i):
                print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))
        g.display()

    def test_breadth_first_traversal(g):
        breadth_first(g, 2)

    def test_depth_first_traversal(g):
        visited = np.zeros(g.num_vertices)
        depth_first(g, visited)

    def test_topological_sort(g):
        topological_sort(g)

    def main():
        num_vertices = 9

        g = AdjacencySetGraph(num_vertices, directed=True)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 7)
        g.add_edge(2, 4)
        g.add_edge(2, 3)
        g.add_edge(1, 5)

        g.add_edge(5, 6)
        g.add_edge(3, 6)
        g.add_edge(3, 4)
        g.add_edge(6, 8)

        test_graph(g)
        test_breadth_first_traversal(g)
        test_depth_first_traversal(g)
        test_topological_sort(g)

    main()
