##the first 'Graph' represents 'Graph.py',
##the second 'Graph' is the class name of 'Graph'
from Graph import Graph
from Digraph import Digraph
class Depth_First_Search():
    def __init__(self, G, s):
        ##A dictionary makes the program able to handle char symbles as the vertices
        self.marked = {} 
        self.edge_To = {}
        for v in G.get_adj_list():
            self.marked[v] = False
            self.edge_To[v] = None
        
        #self.marked = [False] * G.get_Vertices()
        #self.edge_To = [None] * G.get_Vertices() ##create empty list with certain 
        self.s = s ##s is the starting point of the depth first search
        self.cnt = 0
        self.dfs(G, s)

    def __str__(self):
        pass

    def is_marked(self, v):
        return self.marked[v]
    
    def dfs(self, G, v):        
        self.marked[v] = True
        self.cnt += 1        
        for item in G.get_adj_list()[v]:     
            if not self.is_marked(item):
                self.edge_To[item] = v
                self.dfs(G, item)

    def get_cnt(self):
        return self.cnt

    
    def path_to(self, v):
        path = []
        if self.edge_To[v] == None:
            return None
        else:
            while v is not self.s:
                path.append(v)
                v = self.edge_To[v]
            path.append(self.s)
        return path

## show the path for each item in the graph
    def show_path_to(self, G):
        
        for vertice in G.get_adj_list():
            
            if self.path_to(vertice) == None:
                print 'From '+ str(self.s) + ' to ' +str(vertice) + ': ', 'None'
                
            else:
                path = self.path_to(vertice)
                path.reverse()               
                #'->'.join(path)
                print 'From '+ str(self.s) + ' to ' +str(vertice) + ': ', path

    
def main():
    filename = raw_input('input the graph path: ')
    ##G = Digraph(filename)
    G = Graph(filename)
    print 'The adjacency list of the input Graph is: \n'
    print G.adj
    print G
    print ''

    Start_point = raw_input('input the start point: ')

    DFS = Depth_First_Search(G, (Start_point))
    DFS.show_path_to(G)

main()

        
        
        
    
