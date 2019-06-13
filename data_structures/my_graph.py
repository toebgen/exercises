class MyGraphNode():
    """
    A single node of a directed graph
    """

    def __init__(self, data=None, adjacents=None, visited=False):
        self.data = data
        if adjacents == None:
            self.adjacents = []
        else:
            self.adjacents = adjacents
        self.visited = visited
    

    def clear_adjacents(self):
        self.adjacents = []



class MyGraph():
    """
    Directed Graph
    """

    def __init__(self, nodes=None):
        if (nodes==None):
            self.nodes = []
        else:
            self.nodes = nodes
    

    def to_dict(self):
        # the_dict = {node: node.adjacents for node in self.nodes}
        the_dict = {}
        for node in self.nodes:
            adjacent_ids = []
            for adjacent in node.adjacents:
                adjacent_ids.append(adjacent.data)
            the_dict[node.data] = adjacent_ids
        return the_dict


    @classmethod
    def from_dict(cls, the_dict):
        """
        Need to make sure to create every MyGraphNode instance only once.
        E.g.: ID 2 as key in the_dict should refer to the same Node as ID as adjacent in
        the_dict.
        Hence, first create individual MyGraphNode instances for all occurring
        IDs first, then arrange them in a MyGraph.
        """
        graph = cls()

        # 1. Get all occurring node ID's
        all_node_ids = set()
        for node_id, adjacent_ids in the_dict.items():
            all_node_ids.add(node_id)
            for adjacent_id in adjacent_ids:
                all_node_ids.add(adjacent_id)
        node_instances_dict = {node_id: MyGraphNode(node_id) for node_id in all_node_ids}

        # 2. Create the graph using the unique MyGraphNode instances
        for node_id, adjacents in the_dict.items():
            node = node_instances_dict[node_id]
            for adjacent_id in adjacents:
                node.adjacents.append(node_instances_dict[adjacent_id])
            graph.nodes.append(node)

        return graph
    