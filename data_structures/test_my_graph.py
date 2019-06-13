import unittest


from my_graph import MyGraph, MyGraphNode


class TestMyGraphNode(unittest.TestCase):
    def test_instantiation(self):
        node = MyGraphNode()
        self.assertIsNotNone(node)
        del node

        data = 3
        node = MyGraphNode(data)
        self.assertIsNotNone(node)
        self.assertEqual(data, node.data)


class TestMyGraph(unittest.TestCase):
    def setUp(self):
        self.graph_as_dict = self.create_graph_as_dict()
        self.graph = MyGraph().from_dict(self.graph_as_dict)
    

    def create_graph_as_dict(self):
        """
        0 -> 1 -> 2 <- 4
                  ^
                  |
               -> 3
        """
        nodes = [MyGraphNode(i) for i in range(5)]
        graph_as_dict = {
            nodes[0]: [nodes[1]],
            nodes[1]: [nodes[2], nodes[3]],
            nodes[3]: [nodes[2]],
            nodes[4]: [nodes[2]],
        }
        return graph_as_dict
    

    def test_instantiation(self):
        graph = MyGraph()
        self.assertIsNotNone(graph)


if __name__ == "__main__":
    unittest.main()
