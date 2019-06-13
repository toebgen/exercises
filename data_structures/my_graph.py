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


    @classmethod
    def from_dict(cls, the_dict):
        graph = cls()
        for node, adjacents in the_dict.items():
            for adjacent in adjacents:
                node.adjacents.append(adjacent)
            graph.nodes.append(node)
        return graph
    