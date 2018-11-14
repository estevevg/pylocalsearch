from localsearch import LocalSearch
from node import Node
from nodes import Nodes
import random as rnd
import json

## CLASSES REDIFINITION

class ENode(Node):

    def do(self):
        print("Doing "+self.key+" "+str(self.data))

    def isValid(self):
        return self.data

class ENodes(Nodes):

    def h(self, nodes):
        ret = []
        for n in nodes:
            if "val" in n.key:
                ret.append(n)
        return ret

## MAIN FUNCTIONS

def createNode(it, end):
    val = rnd.random()
    n = None
    if val > 0 and val < 0.7:
        n = ENode("val"+str(it), end)
    else:
        n = ENode("not"+str(it), end)
    return n

def createChildren(node, nchild, it, end):
    if end <= it:
        for i in range(nchild):
            fin = (it == end)
            n = createNode(it, fin)
            nextIt = end+1
            createChildren(n, nchild, it, nextIt)
            node.addChildren(n)
    return node



def main():
    nchildren = 10
    it = 10
    nodes = ENodes()
    for i in range(1):
        n = createNode(0, False)
        n = createChildren(n, nchildren, it, 0)
        nodes.addNode(n)

    #search = LocalSearch(nodes)
    #solution = search.initExperiment()

    #print(solution.key)


if __name__ == '__main__':
    main()
