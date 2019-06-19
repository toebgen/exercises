import unittest


from my_graph import MyGraph, MyGraphNode, MyGraphSearch


class HelperMethods():
    """ Collection of helpers. """

    def create_graph_as_dict():
        """
        # 0 --0.1--> 1 --0.2--> 2 <--0.3-- 4
        #              \        ^
        #               0.5     |
        #                  \   0.4
        #                    \  |
        #                     > 3
        """
        graph_as_dict = {
            0: [(1, 0.1)],
            1: [(2, 0.2), (3, 0.5)],
            2: [],
            3: [(2, 0.4)],
            4: [(2, 0.3)],
        }
        return graph_as_dict
    

    def create_graph():
        return MyGraph().from_dict(HelperMethods.create_graph_as_dict())


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
        self.graph_as_dict = HelperMethods.create_graph_as_dict()
        self.graph = MyGraph().from_dict(self.graph_as_dict)
    

    def test_instantiation(self):
        graph = MyGraph()
        self.assertIsNotNone(graph)
    

    def test_from_and_to_dict(self):
        # Create a MyGraph from dict, and then vice versa. Expect the same content.
        graph = MyGraph.from_dict(self.graph_as_dict)
        graph_as_dict = graph.to_dict()
        self.assertEqual(self.graph_as_dict, graph_as_dict)
        self.assertEqual(self.graph.num_nodes, 5)
        

    def test_reset_visited(self):
        self.graph.nodes[1].visited = True
        self.graph.nodes[3].visited = True
        self.assertTrue(self.graph.nodes[1].visited)
        self.assertTrue(self.graph.nodes[3].visited)

        self.graph.reset_visited()
        for node in self.graph.nodes.values():
            self.assertFalse(node.visited)


class TestMyGraphSearch(unittest.TestCase):
    def setUp(self):
        self.graph = HelperMethods.create_graph()

        self.test_cases = [
            #  Defines all im/possible paths in self.graph
            (self.graph.nodes[0], self.graph.nodes[0], True),
            (self.graph.nodes[0], self.graph.nodes[1], True),
            (self.graph.nodes[0], self.graph.nodes[2], True),
            (self.graph.nodes[0], self.graph.nodes[3], True),
            (self.graph.nodes[0], self.graph.nodes[4], False),

            (self.graph.nodes[1], self.graph.nodes[0], False),
            (self.graph.nodes[1], self.graph.nodes[1], True),
            (self.graph.nodes[1], self.graph.nodes[2], True),
            (self.graph.nodes[1], self.graph.nodes[3], True),
            (self.graph.nodes[1], self.graph.nodes[4], False),

            (self.graph.nodes[2], self.graph.nodes[0], False),
            (self.graph.nodes[2], self.graph.nodes[1], False),
            (self.graph.nodes[2], self.graph.nodes[2], True),
            (self.graph.nodes[2], self.graph.nodes[3], False),
            (self.graph.nodes[2], self.graph.nodes[4], False),

            (self.graph.nodes[3], self.graph.nodes[0], False),
            (self.graph.nodes[3], self.graph.nodes[1], False),
            (self.graph.nodes[3], self.graph.nodes[2], True),
            (self.graph.nodes[3], self.graph.nodes[3], True),
            (self.graph.nodes[3], self.graph.nodes[4], False),

            (self.graph.nodes[4], self.graph.nodes[0], False),
            (self.graph.nodes[4], self.graph.nodes[1], False),
            (self.graph.nodes[4], self.graph.nodes[2], True),
            (self.graph.nodes[4], self.graph.nodes[3], False),
            (self.graph.nodes[4], self.graph.nodes[4], True),
        ]


    def test_breadth_first_search(self):
        """ Test all possible paths in graph """
        for case in self.test_cases:
            self.assertEqual(case[2], MyGraphSearch.breadth_first_search(
                self.graph, case[0], case[1]
            ), msg=f'Failed case (src->dest): {case[0].get_id()}->{case[1].get_id()}')


    def test_depth_fist_search(self):
        """ Test all possible paths in graph """
        for case in self.test_cases:
            self.assertEqual(case[2], MyGraphSearch.depth_first_search(
                self.graph, case[0], case[1]
            ), msg=f'Failed case (src->dest): {case[0].get_id()}->{case[1].get_id()}')


if __name__ == "__main__":
    unittest.main()
