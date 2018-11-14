class Nodes:

    def __init__(self):
        self.nodes = []
        self.visited = {}

    def addNode(self, node):
        self.nodes.append(node)

    def visitNode(self, node):
        self.visited[node.key] = node

    def h(self, nodes):
        raise Exception("Not implemented")

    def isVisited(self, node):
        return (node.key in self.visited)
