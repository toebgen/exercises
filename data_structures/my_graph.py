from my_queue import MyQueue


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


    def reset_visited(self):
        self.visited = False


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
            for adjacent_node, adjacent_weight in node.adjacents.items():
                adjacent_ids.append((adjacent_node.id, adjacent_weight))
            the_dict[node_id] = adjacent_ids
        return the_dict
    

    def reset_visited(self):
        """
        Reset visited flags of all nodes.
        """
        for node in self.nodes.values():
            node.visited = False


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
        for node_id, adjacents in the_dict.items():
            all_node_ids.add(node_id)
            for adjacent_id, adjacent_weight in adjacents:
                all_node_ids.add(adjacent_id)
        
        graph.nodes = {node_id: MyGraphNode(node_id) for node_id in all_node_ids}
        graph.num_nodes = len(graph.nodes)

        # 2. Create the graph using the unique MyGraphNode instances
        for node_id, adjacents_with_weights in the_dict.items():
            node = graph.nodes[node_id]
            for adjacent_id, adjacent_weight in adjacents_with_weights:
                node.add_adjacent(graph.nodes[adjacent_id], adjacent_weight)

        return graph


class MyGraphSearch():
    """ Collection of graph searches. """

    @staticmethod
    def breadth_first_search(graph, start_node, destination_node):
        """
        BFS. Make use of a queue, and make sure to mark nodes as
        visited!
        TODO: Return the path and its cost.
        """
        graph.reset_visited()

        q = MyQueue()
        start_node.visited = True
        q.push(start_node)

        while(q.is_empty() == False):
            node = q.pop()
            if (node == destination_node):
                return True
            for adjacent in node.adjacents:
                q.push(adjacent)
        
        return False


    @staticmethod
    def depth_first_search(graph, start_node, destination_node, reset_visited=True):
        """
        DFS. Solve recursively, make sure to mark nodes as visited.
        TODO: Return the path and its cost.
        """
        if reset_visited:
            graph.reset_visited()
        route_found = False

        # print('Working on start_node', start_node.get_id())
        start_node.visited = True

        if (start_node == destination_node):
            # print('Found a path!')
            return True
        if (len(start_node.adjacents) == 0):
                # print("Didn't find a path!")
                return False
        
        for adjacent in start_node.adjacents.keys():
            # keys() are nodes, values() are weights
            # print(f'\tAbout to call adjacent {start_node.get_id()}-> {adjacent.get_id()})')
            route_found = route_found or \
                MyGraphSearch.depth_first_search(graph, adjacent,
                destination_node, reset_visited=False)
            if route_found:
                break
        
        return route_found
