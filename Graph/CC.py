from Graph import Graph

class CC():

    def __init__(self, G):
        self.marked = [False] * G.get_Vertices()
        self.id = {}
        self.cnt = 0
        self.search_components(G)

    def __str__(self):
        s = 'there are ' + str(self.cnt) + ' componnets\n'
        
        for i in self.id:
            s = s + str(i+1) + '#: ' + str(self.id[i])+'\n'

        return s

    def search_components(self, G):
        for v in G.get_adj_list():
            if not self.marked[v]:
                self.id[self.cnt] = []
                self.dfs(G, v)
                self.cnt += 1
 
    def dfs(self, G, v):
        self.marked[v] = True
        
        self.id[self.cnt].append(v)
        for w in G.get_adj_list()[v]:     
            if not self.marked[w]:
                self.dfs(G, w)

    def get_id(self, v):
        return self.id[v]

    def get_components(self):
        return self.cnt


def test():
    filename = raw_input('please input the filename of the graph: ')
    G = Graph(filename)
    print G

    cc = CC(G)
    print cc
    
    

if __name__ == '__main__':
    test()
                
                
            
        
