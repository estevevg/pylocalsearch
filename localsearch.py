class LocalSearch:

    def __init__(self, nodes):
        self.nodes = nodes

    def initExperiment(self):
        for node in self.nodes.nodes:
            if not self.nodes.isVisited(node):
                r = self.iteration(node)
                if r is not None:
                    return r
        return None

    def iteration(self, node):
        node.do()
        if not node.isValid():
            candidates = self.nodes.h(node.getChildren())
            for c in candidates:
                if not self.nodes.isVisited(c):
                    r = self.iteration(c)
                    if r is not None:
                        return r
        else:
            return node
