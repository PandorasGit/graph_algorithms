import unittest


class Vertex:
    """Node in a graph"""

    def __init__(self, name, edges=()):
        self.name = name
        self.edges = edges
        self.visited = None
        self.discovery_time = 0
        self.finishing_time = 0
        self.visited = False
        self.distance = None
        self.parent = None
        self.path = []


class Edge:
    """Edge connecting a vertex to another vertex"""

    def __init__(self, vertex, weight=1):
        self.next_vertex = vertex
        self.weight = weight


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
        m = Vertex("m", (Edge(q), Edge(r), Edge(x)))
        s = Vertex("s", (Edge(r),))
        o = Vertex("o", (Edge(r), Edge(s), Edge(v)))
        n = Vertex("n", (Edge(q), Edge(o)))
        p = Vertex("p", (Edge(o), Edge(s), Edge(z)))
        return [m, q, t, r, u, y, v, w, z, x, n, o, s, p]

    def test_graph_creation_using_vertex(self):
        graph = self.create_graph()
        self.assertEqual(graph[0].edges[0].next_vertex, (graph[1]))

    def test_graph_with_edge(self):
        a = Vertex("a")
        start = Vertex("start", (a,))
        self.assertEqual("a", start.edges[0].name)

    def test_graph_change_discovery_times(self):
        graph = self.create_graph()
        vertex = graph[1]
        vertex.discovery_time = 3
        self.assertNotEqual(vertex.discovery_time, graph[0].discovery_time)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
