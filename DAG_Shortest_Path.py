import math
import unittest
from Vertex import Vertex
from Vertex import Edge


class DAGShortestPath:

    def __init__(self, graph):
        """initializes a graph with distance infinity"""
        for vertex in graph:
            vertex.distance = math.inf
        self.graph = graph

    def relax(self, source, child):
        """Relaxes two vertexes in a graph to tell the distance they have"""
        if child.distance > source.distance + self.calculate_weight(source, child):
            child.distance = source.distance + self.calculate_weight(source, child)
            child.parent = source

    def calculate_weight(self, source, child):
        """Calculates the weight of the edge between two vertices"""
        for edge in source.edges:
            if edge.next_vertex == child:
                return edge.weight
        return None


class TestClass(unittest.TestCase):
    """
    Class for testing Implementation
    """

    @staticmethod
    def create_graph():
        """Creates a directed graph for testing"""
        x = Vertex("x")
        z = Vertex("z")
        w = Vertex("w", (Edge(z),))
        v = Vertex("v", (Edge(w), Edge(x)))
        t = Vertex("t")
        y = Vertex("y", (Edge(v),))
        u = Vertex("u", (Edge(t),))
        r = Vertex("r", (Edge(u), Edge(y)))
        q = Vertex("q", (Edge(t),))
        m = Vertex("m", (Edge(q, 3), Edge(r), Edge(x)))
        s = Vertex("s", (Edge(r),))
        o = Vertex("o", (Edge(r), Edge(s), Edge(v)))
        n = Vertex("n", (Edge(q), Edge(o)))
        p = Vertex("p", (Edge(o), Edge(s), Edge(z)))
        return [m, q, t, r, u, y, v, w, z, x, n, o, s, p]

    def test_relax(self):
        graph = self.create_graph()
        dag_object = DAGShortestPath(graph)
        graph[0].distance = 0
        dag_object.relax(graph[0], graph[1])
        self.assertEqual(3, graph[1].distance)

    def test_weight(self):
        graph = self.create_graph()
        graph[0].distance = 0
        graph[1].distance = math.inf
        dag_object = DAGShortestPath(graph)
        self.assertEqual(3, dag_object.calculate_weight(graph[0], graph[1]))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
