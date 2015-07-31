'''This is Kosaraju algorithms to find out the strong connected components in a di-graph'''



from Digraph import Digraph
from Depth_First_Order import Depth_First_Order

 
class KosarajuSCC():
    def __init__(self, G):
        self.marked = [False] * G.get_Vertices()
        self.id = [None] * G.get_Vertices()
        self.cnt = 0
        
        dfo = Depth_First_Order(G.reverse())
        
        self.search_by_topo_order(G, dfo.topo_list())

    def __str__(self):
        pass

    def search_by_topo_order(self, G, topo_list):
        print topo_list
        for v in topo_list:
            if not self.marked[v]:
                self.dfs(G, v)
                self.cnt += 1

    def dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.cnt
        for w in G.get_adj_list()[v]:
            if not self.marked[w]:
                self.dfs(G, w)
             
    def get_cnt(self):
        return self.cnt

    def get_id(self, v):
        return self.id[v]
    
    def show_components(self):
        s = [''] * self.cnt
        for i in range(0, self.cnt):
            for j in range(0, len(self.id)):
                if self.id[j] == i:
                    s[i] = s[i] + str(j) + ' '
        print 'The strongly connected components are: '
        for k in range(0, len(s)):
            print s[k]
            
    def is_SCC(self, w, v):
        return self.id[w] == self.id[v]


def test():
    G = Digraph('tinyDG.txt')
    print G
    print ''


    kscc = KosarajuSCC(G)
    print '\nThe number of strong connected components: '
    print kscc.get_cnt()
    kscc.show_components()
   
    
if __name__ == '__main__':    
    test()
