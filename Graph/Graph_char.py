''' Read a .txt file and translate it to a graph'''

class Graph():
    def __init__(self, filename = None):
        self.V = 0  #-- num of vertices
        self.E = 0  #-- num of edges
        self.adj = {}
        if not filename == None:
            self.read_data(filename)
            
    def read_data(self, filename):    
        fhand = open(filename)        
        self.V = int(fhand.readline())      
        self.E = int(fhand.readline())        
        
        for i in range(0, self.E):
            string = fhand.readline()
            string = string.strip()
            string = string.split(' ')
            ## the two vertices was seperated by ' '.
            v = (string[0])
            w = (string[1])
            
        ## if vertices was not created yet,
        ## have to create a empty list for that vertice
        
            if v not in self.adj:                
                self.adj[v] = []               
            if w not in self.adj:
                self.adj[w] = []

            self.adj[v].append(w)
            self.adj[w].append(v)
        
    def __str__(self):
        
        s = '\nVertices: ' + str(self.V) + '\n'+\
            'Edges: ' + str(self.E) + '\n'
        for item in self.adj:
            s = s + str(item) + ':' + str(self.adj[item]) + '\n'
        return s

    def add_Edge(self, v , w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
        
    def get_Vertices(self):
        return self.V
    def get_Edges(self):
        return self.E
    
    ## return the adjacency list of the graph
    ## return the self.adj[v] of the adjacency points of point v
    def get_adj_list(self):
        return self.adj

def main():
    try:
        filename = raw_input('please input file name: ')
        G = Graph(filename)
        print G
        print type(G) ## G is object of class 'Graph'
        print type(G.adj) ## G.adj is a dictionary
        
    except:
        print 'can not find the file: ' + filename
    
if __name__ == '__main__':

    main()
