class Digraph():
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
            string = string.split(' ')
            ## the two vertices was seperated by ' '.
            v = int(string[0])
            w = int(string[1])
            
        ## if vertices was not created yet,
        ## have to create a empty list for that vertice
        
            if v not in self.adj:                
                self.adj[v] = []               
            if w not in self.adj:
                self.adj[w] = []

            self.adj[v].append(w)
            #self.adj[w].append(v)
        
    def __str__(self):
        
        s = 'Vertices: ' + str(self.V) + '\n'+\
            'Edges: ' + str(self.E) + '\n'
        for item in self.adj:
            s = s + str(item) + ':' + str(self.adj[item]) + '\n'
        return s
        
    # add an edge from v pointing to w.
    def add_Edge(self, v, w):
        self.adj[v].append(w)
        #self.adj[w].append(v)
        self.E += 1
        
    def get_Vertices(self):
        return self.V
    def get_Edges(self):
        return self.E
    def set_V(self, x):
        self.V = x
    def set_E(self, x):
        self.E = x
    def set_adj(self, x):
        self.adj = x

    def get_adj_list(self):
        return self.adj
    
    ## return a reverse digraph of the original one

    def reverse(self):
        R = Digraph()
        R.set_V(self.get_Vertices())
        R.set_E(self.get_Edges())
        R_adj = {}
        for v in self.adj:            
            R_adj[v] = []  ##set each key as an empty list
            
        for v in self.adj:
            for w in self.adj[v]:
                R_adj[w].append(v)
        R.set_adj(R_adj)
        
        return R
        
            

def main():
    
    try:
        filename = raw_input('please input file name: ')
        G = Digraph(filename)
    except:
        print 'can not find the file: ' + filename
        
    print G        
    print type(G) ## G is object of class 'Graph'
    print type(G.adj) ## G.adj is a dictionary
    print '\nthe reverse digraph of G is: '
    print G.reverse()
    print ''
    print G
   
if __name__ == '__main__':

    main()
