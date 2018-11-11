class Node:

    ##
    # @key: node identifier
    # @data: data set that is needed to check if it works
    ##
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.children = []

    def addChildren(self, child):
        self.children.append(child)

    def getChildren(self):
        return children

    def do(self):
        raise Exception("Needs to be implemented by user")

    def isValid(self):
        raise Exception("Needs to be implemented by user")
