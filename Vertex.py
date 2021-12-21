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
        return [Vertex("p", [("o", 1), ("s",), ("z", 1)]), Vertex("n", [("o",), ("u", 1), ("q", 1)]),
                Vertex("o", [("r", 1), ("s", 1)]), Vertex("s", [("r", 1)]),
                Vertex("m", [("q", 1), ("r", 1), ("x", 1)]), Vertex("r", [("u", 1), ("y", 1)]),
                Vertex("y", [("v", 1)]), Vertex("v", [("x", 1), ("w", 1)]),
                Vertex("w", [("z", 1)]), Vertex("z"), Vertex("u", [("t", 1)]),
                Vertex("q", [("t", 1)]), Vertex("t")]

    def test_graph_creation_using_vertex(self):
        graph = self.create_graph()
        self.assertEqual(graph[0].edges, [("o", 1), ("s",), ("z", 1)])

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
