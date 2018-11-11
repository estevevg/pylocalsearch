class LocalSearch:

    def __init__(self, nodes):
        self.nodes = nodes

    def initExperiment(self):
        for node in self.nodes.nodes:
            if not self.nodes.isVisited(node):
                iteration(node)

    def iteration(self, node):
        node.do()
        if not node.isValid():
            candidates = nodes.h(node.getChildren())
            for c in candidates:
                if not nodes.isVisited():
                    iteration(c)
