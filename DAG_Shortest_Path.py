import math
import unittest
from Vertex import Vertex
from Vertex import Edge
from collections import deque
from Depth_First_Search import DFS


class DAGShortestPath:

    def __init__(self, graph):
        """initializes a graph with distance infinity"""
        for vertex in graph:
            vertex.distance = math.inf
        dfs = DFS(graph)
        self.graph = dfs.topological_sort()

    def relax(self, source, child):
        """Relaxes two vertexes in a graph to tell the distance they have"""
        if child.distance > source.distance + self.calculate_weight(source, child):
            child.distance = source.distance + self.calculate_weight(source, child)
            child.parent = source

    @staticmethod
    def calculate_weight(source, child):
        """Calculates the weight of the edge between two vertices"""
        for edge in source.edges:
            if edge.next_vertex == child:
                return edge.weight
        return math.inf

    def walk_shortest_path(self):
        """Creates the shortest path tree"""
        self.graph[0].distance = 0
        graph_queue = deque(self.graph)
        for vertex in self.graph:
            if vertex in graph_queue:
                graph_queue.popleft()
                for edge in vertex.edges:
                    self.relax(vertex, edge.next_vertex)

    def create_shortest_path_tree(self):
        """Create tree for whole graph"""
        def walk_path(vertex):
            """Create Shortest Path Array"""
            if vertex.parent is None:
                if not vertex.path:
                    vertex.path.append(vertex)
                return
            walk_path(vertex.parent)
            for node in vertex.parent.path:
                if node not in vertex.path:
                    vertex.path.append(node)
            vertex.path.append(vertex)

        for each in self.graph:
            walk_path(each)



class TestClass(unittest.TestCase):
    """
    Class for testing Implementation
    """

    @staticmethod
    def create_graph():
        """Creates a directed graph for testing"""
        z = Vertex("z")
        y = Vertex("y", (Edge(z, 4),))
        x = Vertex("x", (Edge(z, -2), Edge(y, 1)))
        t = Vertex("t", (Edge(z, 6), Edge(y, -1), Edge(x, 3)))
        s = Vertex("s", (Edge(t), Edge(x, 4)))
        r = Vertex("r", (Edge(s, 3), Edge(y, 5), Edge(t, 3)))
        q = Vertex("q", (Edge(x, 5), Edge(r, 1)))
        return [q, r, s, t, x, y, z]

    def test_relax(self):
        graph = self.create_graph()
        dag_object = DAGShortestPath(graph)
        graph[0].distance = 0
        vertex_source = graph[0]
        vertex_child = graph[4]
        dag_object.relax(vertex_source, vertex_child)
        self.assertEqual(5, vertex_child.distance)

    def test_weight(self):
        graph = self.create_graph()
        graph[0].distance = 0
        dag_object = DAGShortestPath(graph)
        dag_object.walk_shortest_path()
        self.assertEqual(1, dag_object.calculate_weight(graph[0], graph[1]))

    def test_shortest_path_for_single_vertex(self):
        dag_object = DAGShortestPath(self.create_graph())
        dag_object.walk_shortest_path()
        self.assertEqual(3, dag_object.graph[6].distance)

    def test_shortest_path_for_paths(self):
        """Failing test, unsure how to create path"""
        dag_object = DAGShortestPath(self.create_graph())
        dag_object.walk_shortest_path()
        dag_object.create_shortest_path_tree()
        actual_name_array = []
        for vertex in dag_object.graph[6].path:
            actual_name_array.append(vertex.name)
        self.assertEqual(["q","x","z"], actual_name_array)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
