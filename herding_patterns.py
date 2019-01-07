
class Node():
    def __init__(self, nodeId, baseSequence):
        self.nodeId = nodeId
        self.pathNode = baseSequence
        self.neighbors = [] # append to add tupples of (nodeId, baseSequence)

class Graph:
    def __init__(self):
        self.nodes = {'0': Node('0','')} 
        self.n_nodes = 0

    def createNode(self, adjacentTo, baseSequence):
        """ Creates a node for the graph and appends it to the parent node """
        self.n_nodes += 1
        self.nodes[str(self.n_nodes)] = Node(str(self.n_nodes), baseSequence)
        self.nodes[str(adjacentTo)].neighbors.append((self.n_nodes, baseSequence))
    
    def verifyPathAdjacentNodes(self, idNode, baseSequence):
        verify = True
        if len(self.nodes[str(idNode)].neighbors) == 0:
            return verify, idNode
        else:
            focusNodeId = idNode
            for node in self.nodes[str(idNode)].neighbors:
                if node[1] == baseSequence:
                    verify = False
                    focusNodeId = node[0]
                    break
            return verify, focusNodeId

    def addPatternsToGraph(self, patterns):
        for p in patterns:
            i = 0
            id = 0
            while i < len(p):
                verifyNoPath, focusId = self.verifyPathAdjacentNodes(id, p[i])
                if verifyNoPath:
                    self.createNode(focusId, p[i])
                    id = self.n_nodes
                else:
                    id = focusId
                i += 1

    def printGraph(self):
        for n in self.nodes.keys():
            if len(self.nodes[n].neighbors) > 0:
                for i in range(len(self.nodes[n].neighbors)):
                    print ("{0}->{1}:{2}".format(n, self.nodes[n].neighbors[i][0], self.nodes[n].neighbors[i][1])) 

class Patterns:
    def __init__(self, patterns = []):        
        self.patterns = ['ATAGA', 'ATC', 'GAT',]
        #self.patterns = ['ananas', 'and', 'antenna', 'banana', 'bandana', 'nab', 'nana', 'pan',]

    def getPatterns(self):
        return self.patterns

    @classmethod
    def getPatternsFromFile(cls, filename = 'patterns.txt'):
        patternsFromFile = []
        with open(filename) as f:
            patterns = f.readlines()
        for pattern in patterns:
            patternsFromFile.append(pattern.strip())

        return cls(patternsFromFile)

if __name__ == "__main__":

    graph = Graph()
    patterns = Patterns() # define a priori in the class
    path = '/Users/lvb/Downloads/'
    filename = 'dataset_294_4.txt'
    patterns = Patterns.getPatternsFromFile(path + filename)
    graph.addPatternsToGraph(patterns.getPatterns())
    graph.printGraph()
    