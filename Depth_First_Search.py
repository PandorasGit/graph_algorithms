import unittest
from Vertex import Vertex


class DFS:
    """Class for running DFS and topological sort """
    time = 0

    def __init__(self, graph):
        self.graph = graph

    def dfs(self):
        # the time given by wall clock is shared by all
        # recursive calls
        def visit(node):
            self.time += 1
            node.discovery_time = self.time
            node.visited = True
            for v in node.edges:
                if v.visited is False:
                    visit(v)
            self.time += 1
            node.finishing_time = self.time

        # All nodes are visited!
        for vertex in self.graph:
            if not vertex.visited:
                visit(vertex)

    def topological_sort(self):
        """Sorts keys in graph in descending order by discovery time"""

        self.graph.sort(key=lambda vertex: vertex.finishing_time, reverse=True)
        return self.graph


class TestClass(unittest.TestCase):
    """
    Class for testing Implementation
    """

    @staticmethod
    def create_graph():
        """Creates a directed graph for testing"""
        x = Vertex("x")
        z = Vertex("z")
        w = Vertex("w", [z])
        v = Vertex("v", [w, x])
        t = Vertex("t")
        y = Vertex("y", [v])
        u = Vertex("u", [t])
        r = Vertex("r", [u, y])
        q = Vertex("q", [t])
        m = Vertex("m", [q, r, x])
        s = Vertex("s", [r])
        o = Vertex("o", [r, s, v])
        n = Vertex("n", [q, o])
        p = Vertex("p", [o, s, z])
        return [m, q, t, r, u, y, v, w, z, x, n, o, s, p]

    def test_dfs_keys(self):
        dfs_object = DFS(self.create_graph())
        dfs_object.dfs()
        finish_time_of_m = dfs_object.graph[0].finishing_time
        self.assertEqual(20,finish_time_of_m)

    def test_topological_sort(self):
        dfs_object = DFS(self.create_graph())
        dfs_object.dfs()
        array_of_keys = dfs_object.topological_sort()
        array_test_able = [None for _ in range(len(array_of_keys))]

        for key in array_of_keys:
            index_of_key = array_of_keys.index(key)
            array_test_able[index_of_key] = key.name

        correct_solution = ["p", "n", "o", "s", "m", "r", "y", "v", "x", "w", "z", "u", "q", "t"]
        self.assertEqual(correct_solution, array_test_able)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
