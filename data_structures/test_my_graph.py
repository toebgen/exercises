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
        graph_as_dict = {
            # TODO have the int's here, instead of the actual instances?!
            0: [1],
            1: [2, 3],
            3: [2],
            4: [2],
        }
        return graph_as_dict
    

    def test_instantiation(self):
        graph = MyGraph()
        self.assertIsNotNone(graph)
    

    def test_from_and_to_dict(self):
        # Create a MyGraph from dict, and then vice versa. Expect the same content.
        graph = MyGraph.from_dict(self.graph_as_dict)
        graph_as_dict = graph.to_dict()
        self.assertEqual(self.graph_as_dict, graph_as_dict)


if __name__ == "__main__":
    unittest.main()
