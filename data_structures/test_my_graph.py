import unittest


from my_graph import MyGraph, MyGraphNode


class TestMyGraphNode(unittest.TestCase):
    def test_instantiation(self):
        node = MyGraphNode()
        self.assertIsNotNone(node)
        del node

        id = 3
        node = MyGraphNode(id)
        self.assertIsNotNone(node)
        self.assertEqual(id, node.id)
        self.assertEqual(id, node.get_id())


    def test_str(self):
        id = 3
        node = MyGraphNode(id)
        expected_str = '3 adjacents: []'
        self.assertEqual(expected_str,  str(node))


    def test_add_adjacent(self):
        """
        Notation: node --weight--> adjacent
        0 --0.1--> 1
          --0.5--> 2
        """
        test_nodes = [MyGraphNode(i) for i in range(3)]
        test_weights = [0.1, 0.5]
        node = test_nodes[0]
        node.add_adjacent(test_nodes[1], test_weights[0])
        node.add_adjacent(test_nodes[2], test_weights[1])
        self.assertEqual(node.get_id(), 0)
        self.assertEqual(node.get_weight(test_nodes[1]), test_weights[0])
        self.assertEqual(node.get_weight(test_nodes[2]), test_weights[1])

        node.clear_adjacents()
        self.assertDictEqual(node.adjacents, {})
        self.assertEqual(node.get_id(), 0)



class TestMyGraph(unittest.TestCase):
    def setUp(self):
        self.graph_as_dict = self.create_graph_as_dict()
        self.graph = MyGraph().from_dict(self.graph_as_dict)
    

    def create_graph_as_dict(self):
        """
        # 0 -> 1 -> 2 <- 4
        #           ^
        #           |
        #        -> 3
        TODO: Also test weights
        """
        graph_as_dict = {
            0: [1],
            1: [2, 3],
            2: [],
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
        

    def test_reset_visited(self):
        self.graph.nodes[1].visited = True
        self.graph.nodes[3].visited = True
        self.assertTrue(self.graph.nodes[1].visited)
        self.assertTrue(self.graph.nodes[3].visited)

        self.graph.reset_visited()
        for node in self.graph.nodes.values():
            self.assertFalse(node.visited)



if __name__ == "__main__":
    unittest.main()
