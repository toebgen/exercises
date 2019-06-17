class MyGraphNode():
    """
    A single node (vertex) of a directed graph.
    self.adjacents is supposed to hold only 1 level of children, no children of
    children.
    Uses a dictionary to keep track of the adjacent nodes to which it is
    connected, and the weight of each edge.
    """

    def __init__(self, id=None, adjacents=None, visited=False):
        self.id = id
        if adjacents == None:
            self.adjacents = {}
        else:
            self.adjacents = adjacents
        self.visited = visited
    

    def add_adjacent(self, adjacent, weight=0):
        self.adjacents[adjacent] = weight


    def clear_adjacents(self):
        self.adjacents = {}
    

    def get_id(self):
        return self.id
    

    def get_weight(self, adjacent):
        return self.adjacents[adjacent]
    

    def __str__(self):
        return str(self.id) + ' adjacents: ' + \
            str([x.id for x in self.adjacents])



class MyGraph():
    """
    Directed Graph.
    Holding all nodes of the graph. Implemented as a dict of all node ID's
    mapping to their instances. Adjacents are held in the MyGraphNode instances
    themselves.
    """

    def __init__(self, nodes=None):
        if (nodes==None):
            self.nodes = {}
        else:
            self.nodes = nodes
        self.num_nodes = 0
    

    def add_node(self, id):
        self.num_nodes += 1
        new_node = MyGraphNode(id)
        self.nodes[id] = new_node
        return new_node
    

    def to_dict(self):
        # the_dict = {node: node.adjacents for node in self.nodes}
        the_dict = {}
        for node_id, node in self.nodes.items():
            adjacent_ids = []
            for adjacent in node.adjacents:
                adjacent_ids.append(adjacent.id)
            the_dict[node_id] = adjacent_ids
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
        
        # TODO: Make more efficient, i.e. don't run through dict twice!
        # 1. Get all occurring node ID's
        all_node_ids = set()
        for node_id, adjacent_ids in the_dict.items():
            all_node_ids.add(node_id)
            for adjacent_id in adjacent_ids:
                all_node_ids.add(adjacent_id)
        
        graph.nodes = {node_id: MyGraphNode(node_id) for node_id in all_node_ids}

        # 2. Create the graph using the unique MyGraphNode instances
        for node_id, adjacents in the_dict.items():
            node = graph.nodes[node_id]
            for adjacent_id in adjacents:
                node.add_adjacent(graph.nodes[adjacent_id])

        return graph
    